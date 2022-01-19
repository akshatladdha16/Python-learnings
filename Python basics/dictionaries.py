#dictionaries in python
month_conversion={
    "jan":"January",
    "feb":"Febuary",
    "mar":"March",
    "ap":"April",
    "may":"May"
    #these keys can be anything its same as switch case concept in c++
}
enter_key=input("enter key : ")
print(month_conversion.get(enter_key,"not a valid key"))#get function always allow us to give default value if key is not present
#so if key is not present in dictionary then get function will give something default like " not a valid key"