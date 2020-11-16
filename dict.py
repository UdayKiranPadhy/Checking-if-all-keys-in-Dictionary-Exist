from typing import Dict, Tuple, Union, List
 
 
def missing_params(test_object: Dict = None, ref: Tuple = None) -> Union[List, None]:
    missing = [k for k in ref if k not in test_object]
    return missing if missing else None
 
if __name__ == "__main__":
    payload = dict(
        username="username",
        password="password",
        address="address",
        extra_vars="extra_vars"
    )
 
    required = "username", "password", "address", "special_vars", "index_vars"
 
    missing = missing_params(test_object=payload, ref=required)
    if missing is None:
        print("All params exist.")
    else:
        print(f"The missing params is/are: {', '.join(missing)}")