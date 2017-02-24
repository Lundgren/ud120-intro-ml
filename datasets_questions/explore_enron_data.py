#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle
import math

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

def print_it():
    for x in enron_data:
        print (x)
        for y in enron_data[x]:
            print (y,':',enron_data[x][y])

#print_it()

print "persons:", len(enron_data)
print "features:", len(enron_data["SKILLING JEFFREY K"])

pois = 0
for n in enron_data:
    if enron_data[n]["poi"] == 1:
        pois = pois + 1

print "nbr of poi:", pois

print "stock value James Prentice:", enron_data["PRENTICE JAMES"]["total_stock_value"]

print "Wesley Colwell sent mail to pois:", enron_data["COLWELL WESLEY"]["from_this_person_to_poi"], "times"

print "Jeffrey K Skilling exercised stock:", enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]

print "money for Lay:", enron_data["LAY KENNETH L"]["total_payments"], ", Skilling:", enron_data["SKILLING JEFFREY K"]["total_payments"], " & Fastow:", enron_data["FASTOW ANDREW S"]["total_payments"]

salary = 0
email = 0
for n in enron_data:
    if not enron_data[n]["salary"] == "NaN":
        salary = salary + 1
    if not enron_data[n]["email_address"] == "NaN":
        email = email + 1

print "nbr of salary:", salary, ", email: ", email

total_pay = 0
for n in enron_data:
    if enron_data[n]["total_payments"] == "NaN":
        total_pay = total_pay + 1

print "% not salary:", (total_pay * 100 / len(enron_data)), ", ", total_pay

total_pay_pois = 0
for n in enron_data:
    if enron_data[n]["poi"] == 1:
        if enron_data[n]["total_payments"] == "NaN":
            total_pay_pois = total_pay_pois + 1

print "% not salary & poi:", (total_pay_pois * 100 / pois)