import urllib.request as urllib

print("This is a site connectivity checker program")
input_url = input("Input the url of the site you want to check: ")

def main(url):
    print("Checkingt connectivity")

    response = urllib.urlopen(url)
    print("Connected to", url, "succesfully")
    print("The response code was: ", response.getcode())

main(input_url)
