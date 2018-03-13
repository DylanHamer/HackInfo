"""
HackInfo
Simple system information tool
by Dylan Hamer
"""

import platform  # Get OS information
import getpass  # Get username

informationString = \
"""
OS: {os}
User: {user}
"""

systemInformation = {"os":platform.system(),
                     "version":platform.release(),
                     "user":getpass.getuser()}
            
def formatInfo(informationString):
    os = systemInformation.get("os", "Unknown OS")
    user = systemInformation.get("user", "Unknown User")
    version = systemInformation.get("version", "Unknown Version")
    try:
        informationString = informationString.format(os=os,
                                                     user=user,
                                                     version=version)
    except KeyError as invalidValue:
        print("Error in configuration! {} is not a valid information type.".format(invalidValue))
        return None
    return informationString
 
def main():
    info = formatInfo(informationString)
    if info is not None:
        print(info)

main()
