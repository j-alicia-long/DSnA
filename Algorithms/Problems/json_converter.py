
# Enter your code here. Read input from STDIN. Print output to STDOUT


def dictionaryToJson(input_dict):
    output = ""

    # left bracket
    output += "{"

    # Iterate through content
    for key, value in input_dict.items():
        # add key to output
        output += key + ":"

        # add value to dict
        if type(value) is dict:
            # if value is nested dict, make recursive call to get json
            output += dictionaryToJson(value)
        else:
            output += str(value)

        # concat comma for non-last items
        output += ","

    output = output.rstrip(",")

    # right bracket
    output += "}"

    return output


def jsonToDictionary(input):
    output = {}

    N = len(input)
    # Pointers to keep track of key and value starting indices
    key_index, value_index = 0, 0
    nested_value = False
    key, value = None, None

    for i in range(N):
        curr = input[i]
        if curr.isalpha():
            continue

        # Get key
        if not key:
            # Start index of key
            if curr == "{" or curr == ",":
                key_index = i+1
            # End index of key
            elif curr == ":":
                key = input[key_index:i] # Save key
                value_index = i+1
            continue

        # Get value
        if key and not value:
            # Start index of nested value
            if curr == "{":
                nested_value = True
                continue

            # End index of string value
            elif curr == "," and not nested_value:
                value = input[value_index:i] # Save value

            # End index of last dict value
            elif curr == "}":
                if nested_value:
                    # Recursive call to process nested dict
                    value = jsonToDictionary(input[value_index:i+1])
                else:
                    value = input[value_index:i] # Save value

        # Save to output & reset buffers
        if key and value:
            output[key] = value # Save key-value pair to output
            key, value = None, None # Reset buffers
            nested_value = False
            key_index = i+1 # Reset start index of next key

    return output

sample_dict = {
  "a": "apple",
  "b": {
    "ba": "apple",
    "bb": "blueberry",
    "bc": "cranberry"
  },
  "c": "cranberry"
}
sample_dict_2 = {
  "a": "apple",
  "b": {
    "ba": {
        "baa": 1,
        "bab": "blueberry",
        "bac": "cranberry"
    }
  },
  "c": "cranberry"
}
print(sample_dict_2)
print(dictionaryToJson(sample_dict_2))
print(jsonToDictionary(dictionaryToJson(sample_dict_2)))
