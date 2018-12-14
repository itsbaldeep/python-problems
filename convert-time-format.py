def convert(input_str):
    time = input_str.split(":") # Make a list with three items
    time[2] = time[2][:2] # Removing AM/PM from last item
    time[0] = 0 if time[0] == "12" else int(time[0]) # Reset to 0 hours if noon or midnight
    if "pm" in input_str.lower(): time[0] += 12 # If PM, then add 12
    time[0] = "0"+str(time[0]) if time[0]/10 < 1 else str(time[0]) #Optional formatting
    return ":".join(time) #Returning a string


# Call the convert function with any time as argument
converted = convert("01:24:10AM")
print(converted)
# It prints the 24-hour formatted time
