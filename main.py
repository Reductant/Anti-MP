# -*- coding: utf-8 -*-
"""
This module provides a flask application
that allows people to run the program
in the browser.

"""

from flask import Flask, request, render_template

from functools import lru_cache

import antimp


app = Flask(__name__)


@app.route('/')
def home():
    """Render the homepage"""
    return render_template('index.html')


@app.route('/check')
def check():
    """Render the form with issues"""
    return render_template('form.html',
                           issues=enumerate(antimp.issue_list),
                           num_questions=len(antimp.issue_list))


@app.route('/results', methods=['POST'])
def process():
    """Process the results from the user"""
    # TODO: optimise for speed
    user_data = request.form.copy()
    mp_data = antimp.get_mp_data()
    choices = {
        'yes': 1,
        'no': -1,
        'undecided': 0
    }

    assert len(user_data) == len(antimp.issue_list)

    for i, (issue, slug) in enumerate(antimp.issue_list):
        key = 'question_{0}'.format(i)
        selected = user_data[key]
        user_choice = choices[selected]

        for mp_record in mp_data:
            opinion = get_agreement(mp_record[4], slug)
            mp_record[5] += (opinion * user_choice)

    mp_data.sort(key=lambda x: x[5])

    return render_template('results.html', results=mp_data)


@lru_cache(700)
def get_agreement(html, issue):
    a = html.split("<li>")

    voted = []
    for i in a:
        if "voted" in i:
            voted.append(i.split("<a class")[0])

    opinion = 0
    for i in voted:
        if issue in i:
            if "voted for" in i:
                opinion = 1
            if "voted against" in i:
                opinion = -1

    return opinion


if __name__ == '__main__':
    antimp.check_data()
    app.run()
