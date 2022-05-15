#!/usr/bin/env python3
# Created By: Ferdous Sediqi
# Date: May, 12, 2022
# This program asks the user for their full adress and then 
# display it in a mailing format

# function with apartment number parameter
def format_address_apt(full_name, street_num, street_name, city, province, postal_code, appartement_number):
    print("Your Canadian mailing address is: ")
    print("")
    print(full_name.upper())
    // # check apt-num input
    if appartement_number != "":
        print(appartement_number.upper(),"-",street_num.upper(), "", street_name.upper(),)
        print(city.upper(), "", province.upper(), "", postal_code.upper())
    


# function without apartment number parameter
def format_address(full_name, street_num, street_name, city, province, postal_code):
        print("Your Canadian mailing address is: ")
        print("")
        print(full_name.upper())
        print("-", street_num.upper(), street_name.upper())
        print(city.upper(), "", province.upper(), "", postal_code.upper())


def main():
    # ask for their name
    full_name = input("Enter your full name: ")

    # ask user if they live in an appartment    
    live_in_apt = input("Do you live in an apartment (y/n)? ")

    # check if they live in an apartment or not.
    if live_in_apt == "y":
        apt_num = input("Enter your apartemnt number: ")
        street_num = input("Enter your street number: ")
        street_name = input("Enter your street name (i.e. main st, Lees , Rideau, etc): ")
        city = input("Enter your your city: ")
        province = input("Enter your province (i.e. ON, AB, B.C.) ")
        postal_code = input("Enter your postal code (i.e. K1S5J5): ")
        
        # call the function with apt-num and display address as mailing format        
        format_address_apt(full_name, street_num, street_name, city, province, postal_code, apt_num)
     
    else:
        # ask user information
        street_num = input("Enter your street number: ")
        street_name = input("Enter your street name (i.e. main st, Lees , Rideau, etc): ")
        city = input("Enter your your city: ")
        province = input("Enter your province (i.e. ON, AB, B.C.) ")
        postal_code = input("Enter your postal code (i.e. K1S 5J5): ")
        print("")
        # call the function without apt-num and display address as mailing format 
        format_address(full_name, street_num, street_name, city, province, postal_code)
   

if __name__ == "__main__":
    main()
