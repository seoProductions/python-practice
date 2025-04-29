'''

Python Programing
April 2024

This will write a pogram that creates a dictionary containing the U.S.
states as keys, and their capitals as values. (Use the Internet
Programming assignments:

Write a U.S states quiz game. Nice and simple. I will use python map's/Dictionaries for my assignment
'''
import random


def main():

    dictionary = {
        "Alabama": "Montgomery",
        "Alaska": "Juneau",
        "Arizona": "Phoenix",
        "Arkansas": "Little Rock",
        "California": "Sacramento",
        "Colorado": "Denver",
        "Connecticut": "Hartford",
        "Delaware": "Dover",
        "Florida": "Tallahassee",
        "Georgia": "Atlanta",
        "Hawaii": "Honolulu",
        "Idaho": "Boise",
        "Illinois": "Springfield",
        "Indiana": "Indianapolis",
        "Iowa": "Des Moines",
        "Kansas": "Topeka",
        "Kentucky": "Frankfort",
        "Louisiana": "Baton Rouge",
        "Maine": "Augusta",
        "Maryland": "Annapolis",
        "Massachusetts": "Boston",
        "Michigan": "Lansing",
        "Minnesota": "St. Paul",
        "Mississippi": "Jackson",
        "Missouri": "Jefferson City",
        "Montana": "Helena",
        "Nebraska": "Lincoln",
        "Nevada": "Carson City",
        "New Hampshire": "Concord",
        "New Jersey": "Trenton",
        "New Mexico": "Santa Fe",
        "New York": "Albany",
        "North Carolina": "Raleigh",
        "North Dakota": "Bismarck",
        "Ohio": "Columbus",
        "Oklahoma": "Oklahoma City",
        "Oregon": "Salem",
        "Pennsylvania": "Harrisburg",
        "Rhode Island": "Providence",
        "South Carolina": "Columbia",
        "South Dakota": "Pierre",
        "Tennessee": "Nashville",
        "Texas": "Austin",
        "Utah": "Salt Lake City",
        "Vermont": "Montpelier",
        "Virginia": "Richmond",
        "Washington": "Olympia",
        "West Virginia": "Charleston",
        "Wisconsin": "Madison",
        "Wyoming": "Cheyenne"}
    
    correct_count = 0
    incorrect_count = 0

    while True:

        state = random.choice(list(dictionary))
        print(f"What is the capital of {state}? ")
        answer = input()

        if (answer.lower() == dictionary.get(state).lower()):
            print(f"Correct!")
            correct_count += 1
        else:
            print(f"Wrong, it was {dictionary.get(state)}!")
            incorrect_count += 1
        
        print()
        print(f"Correct-Count {correct_count} : Incorrect Count {incorrect_count}")
        print()

main()
