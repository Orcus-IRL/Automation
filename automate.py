import subprocess
import json


# Part 1:
def crt():
    print("CRT.sh Script processing....")
    try:
        with open("data.json", "r") as file:  # check weather the file exists or not
            data = json.load(file)
    except FileNotFoundError:
        print(
            "data.json file is necessary to run....\nExiting."
        )  # if no file found then throw this error
        exit()
    domains = sorted(
        set(domain for i in data for domain in i["name_value"].split())
    )  # from the json file, get this particular field "name_value"
    with open(
        "crtsh_sd.txt", "w"
    ) as file:  # create a txt file and store the field details in that txt
        file.writelines("\n".join(domains) + "\n")  # file
    with open(
        "crtsh_sd.txt", "r"
    ) as fileread:  # check weather the file has any domains starting with
        lines = (
            fileread.readlines()
        )  # any special character if no then write that line in the same txt file
    filtered_lines = [line for line in lines if line.strip() and line[0].isalnum()]
    with open("crtsh_sd.txt", "w") as file:
        file.writelines(filtered_lines)
    return "Processing complete! Check crtsh.txt \n"


# Part 2
def subfinder():
    print(
        "Subfinder Script processing...."
    )  # a simple subfinder command execution in linux and store the result in a text file
    subfinder_command = (
        f"subfinder -d {domain_name} | grep {domain_name} | sort -u >> subfinder.txt"
    )
    subprocess.run(subfinder_command, shell=True, text=True)
    return "Processing complete! Check subfinder.txt\n"


# Part 3
def assetfinder():
    print(
        "Assetfinder Script processing...."
    )  #  a simple assetfinder command execution in linux and store the result in a text file
    assetfinder_command = (
        f"assetfinder {domain_name} | grep {domain_name} | sort -u >> assetfinder.txt"
    )
    subprocess.run(assetfinder_command, shell=True, text=True)
    return "Processing complete! Check assetfinder.txt\n"


def moveToSingleFile():
    print(
        "Moving files to single file...."
    )  # take all three text file and store the unique elements into one last file
    command = "cat crtsh.txt subfinder.txt assetfinder.txt | sort -u > all_domains.txt"
    subprocess.run(command, shell=True, text=True)
    return "Processing complete! Check all_domains.txt\n"


def http_probe_check():
    print(
        "Checking for alive domains...."
    )  # Check for alive and dead sites and store the result in the text file
    command = "cat all_domains.txt | httprobe -prefer-https >> http_probe_results.txt"
    subprocess.run(command, shell=True, text=True)
    return "Processing complete! Check http_probe_results.txt\n"


print(
    "0 - run all\n1 - run crt script\n1 - run subfinder script\n1 - run assetfinder script\n"
)  # a little menu function just in case if I needed to run any one of the scripts
num = int(input("Enter a value: "))
if num == 0 or num == 1:
    crt()
elif num == 0 or num == 2:
    domain_name = input("Enter domain name: ")
    subfinder()
elif num == 0 or num == 3:
    domain_name = input("Enter domain name: ")
    assetfinder()
else:
    print("Enter a valid input.")

moveToSingleFile()  # these two functions should run no matter what I think but need to check for that
http_probe_check()
