import pandas as pd

def transform_data(raw_json):
    features = raw_json["features"]

    records = []
    for feature in features:
        props = feature["properties"]

        records.append({
            "town": props.get("TOWN"),
            "county": props.get("COUNTY"),
            "state": props.get("STATE")
        })

    df = pd.DataFrame(records)
    return df