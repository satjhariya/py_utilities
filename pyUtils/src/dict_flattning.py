import pandas as pd

def flatten_to_rows(d, parent_keys=None):
    if parent_keys is None:
        parent_keys = []
    rows = []
    if isinstance(d, dict):
        # If all values are not dicts, treat as leaf row
        if all(not isinstance(v, dict) for v in d.values()):
            row = parent_keys + list(d.values())
            rows.append(row)
        else:
            for k, v in d.items():
                rows.extend(flatten_to_rows(v, parent_keys + [k]))
    else:
        # d is a leaf value (not a dict)
        rows.append(parent_keys + [d])
    return rows


if __name__ == "__main__":
    sample_dict = {
    "x":{"j":{'a': {'p': 10, 'q': 20},
            'b':{'p': 30, 'q': 40},
            'c': {'p': 50, 'q': 60}},
        "k":{'a': {'p': 100, 'q': 200},
            'b':{'p': 300, 'q': 400},
            'c': {'p': 500, 'q': 600}},    
        "l":{'a': {'p': 1000, 'q': 2000},
            'b':{'p': 3000, 'q': 4000},
            'c': {'p': 5000, 'q': 6000}}},
    "y":{"j":{'a': {'p': -10, 'q': -20},
            'b':{'p': -30, 'q': -40},
            'c': {'p': -50, 'q': -60}},
        "k":{'a': {'p': -100, 'q': -200},
            'b':{'p': -300, 'q': -400},
            'c': {'p': -500, 'q': -600}},    
        "l":{'a': {'p': -1000, 'q': -2000},
            'b':{'p': -3000, 'q': -4000},
            'c': {'p': -5000, 'q': -6000}}}
        }
#  """
#  """
#     expected output:
#     local1 local2  p   q
#        j      a   10  20
#        j      b   30  40
#        j      b   50  60
#        k      a   100 200
#        k      b   300 400
#        k      b   500 600
#       
#  """
    # flattener = dict_flattning()
    flat_dict = flatten_to_rows(sample_dict)
    df = pd.DataFrame(flat_dict)
    df.columns = ['loca1', 'local2', 'local3', 'p', 'q']
    print("Flattened Dictionary:")
    print(df)
    df.to_csv("flattened_dict_data.csv", index=False)