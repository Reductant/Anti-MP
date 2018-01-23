# -*- coding: utf-8 -*-
"""
This module provides a command line interface
that allows people to run the program.

It also contains most of the logic.

"""
import csv
import urllib.request
from csv import reader as csvreader
from operator import itemgetter
import os.path


def get_mp_urls(url):
    response = urllib.request.urlopen(url)
    data = response.read()
    text = data.decode("utf-8")

    firstlist = text.split("\n")

    # Extract names and urls

    url_list = []
    for i in firstlist:
        if 'href="/mp/' in i:
            x = 'https://www.theyworkforyou.com' + i.split('href="')[1].split('"')[0] + '/votes'
            url_list.append(x)

    name_list = []
    for i in firstlist:
        if '<h2 class="people-list__person__name">' in i:
            x = i.split('name">')[1].split('<')[0]
            name_list.append(x)

    party_list = []
    for i in firstlist:
        if '<span class="people-list__person__party' in i:
            x = i.split('party ')[1].split('">')[0]
            party_list.append(x)

    url_name_list = []
    print(len(url_list), len(name_list))
    x = 0
    while x < len(name_list):
        url_name_list.append([name_list[x], 0, party_list[x], url_list[x]])
        x += 1

    return url_name_list


def get_page(url):
    response = urllib.request.urlopen(url)
    data = response.read()
    text = data.decode("utf-8")
    text = text.replace("\n", "")
    text = text.replace(",", "")
    text = text.replace("\t", "")
    return text


def preloader():
    names = get_mp_urls("https://www.theyworkforyou.com/mps/")

    # Acquire HTML data for each entry in the names list
    count = 0
    while count < len(names):
        names[count].append(get_page(names[count][3]))
        print(count, names[count][0])
        count += 1

    with open("antimp.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(names)


issue_list = [
    ("Are you in favour of the removal of hereditary peers from the House of Lords?", "hereditary peers"),
    ("Are you in favour of reducing the rate of corporation tax?", "corporation tax"),
    ("Are you in favour of equal gay rights?", "gay rights"),
    ("Are you in favour of equal marriage between two people of the same sex?", "two people of same sex"),
    ("Are you in favour of laws to promote equality and human rights?", "equality and human rights"),
    ("Are you in favour of allowing terminally ill people to be given assistance to end their life?", "end their life"),
    ("Are you generally in favour of the use of UK military forces in combat operations overseas?", "combat operations overseas"),
    ("Are you in favour of investigations into the Iraq war?", "into the Iraq war"),
    ("Are you in favour of replacing Trident with a new nuclear weapons system?", "Trident"),
    ("Are you in favour of more EU integration?", "EU integration"),
    # ("Are you in favour of a referendum on the UK's membership of the EU?", "referendum on the UK's membership"),
    ("Are you in favour of strengthening the Military Covenant?", "Military Covenant"),
    ("Are you in favour of the right to remain of EU nationals already living in the UK?", "right to remain for EU nationals"),
    ("Are you in favour of UK membership of the EU?", "UK membership of the EU"),
    ("Are you in favour of miliraty action against ISIL (Daesh)?", "ISIL"),
    ("Are you in favour of reducing housing benefit for social tenants deemed to have excess bedrooms (which Labour describe as the 'bedroom tax')?", "bedroom tax"),
    ("Are you in favour of raising welfare benefits at least in line with prices?", "at least in line with prices"),
    ("Are you in favour of paying higher benefits over longer periods for those unable to work due to illness or disability?", "illness or disability"),
    ("Are you in favour of making local councils responsible for helping those in financial need afford their council tax and reducing the amount spent on such support?", "amount spent on such support"),
    ("Are you in favour of a reduction in spending on welfare benefits?", "welfare benefits"),
    ("Are you in favour of spending public money to create guaranteed jobs for young people who have spent a long time unemployed?", "guaranteed jobs for young people"),
    ("Are you in favour of raising the threshold at which people start to pay income tax?", "raising the threshold at which people"),
    ("Are you in favour of increasing the rate of VAT?", "rate of VAT"),
    ("Are you in favour of higher taxes on alcohol drinks?", "alcoholic drinks"),
    ("Are you in favour of higher taxes on plane tickets?", "plane tickets"),
    ("Are you in favour of lower taxes on fuel for motor vehicles?", "fuel for motor"),
    ("Are you in favour of increasing the tax rate applied to income over £150,000?", "150000"),
    ("Are you in favour of encouraging occupational pensions?", "occupational pensions"),
    ("Are you in favour of automatic enrolment in occupational pensions?", "automatic enrolment"),
    ("Are you in favour of a bankers' bonus tax?", "bonus tax"),
    ("Are you in favour of higher taxes on banks?", "taxes on banks"),
    ("Are you in favour of an annual tax on the value of expensive homes (popularly known as a mansion tax?)", "mansion tax"),
    ("Are you in favour of allowing employees to exchange some employment rights for shares in the company they work for?", "rights for shares"),
    ("Are you in favour of more restrictive regulation of trade union activity?", "regulation of trade union activity"),
    ("Are you in favour of reducing capital gains tax?", "capital gains tax"),
    ("Are you in favour of reducing the rate of corporation tax?", "corporation tax"),
    ("Are you in favour of measures to reduce tax avoidance?", "tax avoidance"),
    ("Are you in favour of stronger tax incentives for companies to invest in assets?", "companies to invest"),
    ("Are you in favour of a new high speed rail infrastructure?", "high speed rail"),
    ("Are you in favour of restricting the provision on services to private patients by the NHS?", "private patients"),
    ("Are you in favour of reforming the NHS so GPs buy services behalf of their patients?", "behalf of their patients"),
    ("Are you in favour of smoking bans?", "smoking bans"),
    ("Are you in favour of greater autonomy for schools?", "autonomy for schools"),
    ("Are you in favour of raising England's undergraduate tuition fee cap to £9,000 per year?", "9000"),
    ("Are you in favour of academy schools?", "academy schools"),
    ("Are you in favour of ending financial support for some 16-19 year olds in training and further education?", "16-19"),
    ("Are you in favour of university tuition fees?", "tuition fees"),
    ("Are you in favour of reducing central government funding of local government?", "funding of local government"),
    ("Are you in favour of there being an equal number of electors per parliamentary constituency?", "number of electors"),
    ("Are you in favour of there being fewer MPs in the House of Commons?", "fewer MPs"),
    ("Are you in favour of a more proportional system for electing MPs?", "proportional system"),
    ("Are you in favour of a wholly elected House of Lords?", "wholly elected"),
    ("Are you in favour of local councils keeping money raised from taxes on business premises in their areas?", "taxes on business premises"),
    ("Are you in favour of greater restrictions on campaigning by third parties, such as charities, during elections?", "campaigning by third parties"),
    ("Are you in favour of fixed periods between parliamentary elections?", "fixed periods between"),
    ("Are you in favour of transferring more powers to the Welsh Assembly?", "Welsh Assembly"),
    ("Are you in favour of transferring more powers to the Scottish Parliament?", "Scottish Parliament"),
    ("Are you in favour of more powers for local councils?", "powers for local councils"),
    ("Are you in favour of a veto for MPs from England, Wales and Northern Ireland over laws specifically impacting their part of the UK", "laws specifically impacting"),
    ("Are you in favour of lowering the voting age?", "voting age"),
    ("Are you in favour of a stricter asylum system?", "stricter asylum system"),
    ("Are you in favour of the introduction of elected Police and Crime Commissioners?", "introduction of electe"),
    ("Are you in favour of requiring the mass retention of information about communications?", "information about communications"),
    ("Are you in favour of stronger enforcement of immigration rules?", "immigration rules"),
    ("Are you in favour of mass surveillance of people's communications and activities?", "mass surveillance"),
    ("Are you in favour of merging police and fire services under Police and Crime Commissioners?", "fire service"),
    ("Are you in favour of measures to prevent climate change?", "prevent climate change"),
    ("Are you in favour of selling England's state owned forests?", "forests"),
    ("Are you in favour of financial incentives for low carbon emission electricity generation methods?", "low carbon"),
    ("Are you in favour of culling badgers to tackle bovine tuberculosis?", "tuberculosis"),
    ("Are you in favour of greater regulation of hydraulic fracturing (fracking) to extract shale gas?", "shale gas"),
    ("Are you in favour of greater public control of bus services?", "bus services"),
    ("Are you in favour of slowing the rise in rail fares?", "rail fares"),
    ("Are you in favour of a publicly owned railway system?", "railway system"),
    ("Are you in favour of phasing out secure tenancies for life?", "secure tenancies"),
    ("Are you in favour of charging a market rent to high earners renting a council home?", "high earners renting"),
    ("Are you in favour of greater regulation of gambling?", "regulation of gambling"),
    ("Are you in favour of capping civil service redundancy payments?", "redundancy payments"),
    ("Are you in favour of Labour's anti-terrorism laws?", "anti-terrorism laws"),
    ("Are you in favour of the privatisation of Royal Mail?", "Royal Mail"),
    ("Are you in favour of requiring pub companies to offer pub landlords rent-only leases?", "rent-only leases"),
    ("Are you in favour of restricting the scope of legal aid?", "legal aid"),
    ("Are you in favour of allowing national security sensitive evidence to be put before courts in secret sessions?", "secret sessions"),
    ("Are you in favour of a statutory register of lobbyists?", "register of lobbyists"),
    ("Are you in favour of limits on success fees paid to lawyers in no-win no fee cases?", "fee cases"),
    ("Are you in favour of restrictions on fees charged to tenants by letting agents?", "letting agents")
]


def get_agreement(li, mp_number, issue):
    a = li[mp_number][4].split("<li>")

    voted = []
    for i in a:
        if "voted" in i:
            voted.append(i.split("<a class")[0])

    opinion = 0
    for i in voted:
        if issue[1] in i:
            if "voted for" in i:
                opinion = 1
            if "voted against" in i:
                opinion = -1

    return opinion


def run():
    check_data()

    li = get_mp_data()

    print("Please enter your name:")
    user_name = input()

    issue_count = 0
    for issue in issue_list:
        issue_count += 1
        print()
        print("Question", issue_count, "of", len(issue_list))
        print(issue[0])
        print("Type Y/N or press ENTER to skip")

        selection = input()

        if selection.upper() == "Y":
            user_choice = 1
        elif selection.upper() == "N":
            user_choice = -1
        else:
            user_choice = 0

        mp_number = 0
        while mp_number < len(li):
            opinion = get_agreement(li, mp_number, issue)
            li[mp_number][5] += (opinion * user_choice)
            mp_number += 1

    final_csv = []
    for i in li:
        final_csv.append([i[0], i[2], i[5]])

    final_csv = sorted(final_csv, key=itemgetter(2))

    final_csv = [["Name", "Party", "Score"]] + final_csv

    for i in final_csv:
        print(i)

    with open(user_name + ".csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(final_csv)

    print()
    print("Your results are saved as " + user_name + ".csv")
    print()
    print("Press ENTER to exit")
    _ = input()


def get_mp_data():
    with open("antimp.csv") as fp:
        reader = csvreader(fp)
        li = list(reader)
    for i in li:
        i.append(0)
    return li


def check_data():
    if not os.path.isfile("antimp.csv"):
        print("The first time this program is run, it needs to download fresh data from Theyworkforyou.com.")
        print("This may take a few minutes.")
        print()
        print("Press ENTER to begin")
        _ = input()  # underscore if often used as in "don't care" variable
        preloader()
        print()
        print("That's done! The data has been saved permanently, so it won't take so long next time.")


if __name__ == '__main__':
    run()
