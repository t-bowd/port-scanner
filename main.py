import sys
import socket
import pyfiglet
from datetime import datetime


if __name__ == "__main__":
    # ASCII Banner
    ascii_banner = pyfiglet.figlet_format('PORT SCANNER')
    print(ascii_banner)

    # Define Target
    if len(sys.argv) == 2:

        # Translate hostname to IPv4
        target = socket.gethostbyname(sys.argv[1])

    else:
        print("Invalid amount  of arguments")

    # Add banner
    print("-" * 50)
    print("Scanning target: " + target)
    print("Scanning started at: " +str(datetime.now()))
    print("-" * 50)

    try:
        # Will try to scan ports between 1 and 65,535
        for port in range(1, 65535):

            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)

            # Returns error indicator
            result = s.connect_ex((target, port))
            if result == 0:
                print("Port {} is open".format(port))
            s.close()
    except KeyboardInterrupt:
        print("\n Exiting program")
        sys.exit()
    except socket.gaierror:
        print("\n Host name could not be resolved")
        sys.exit()
    except socket.error:
        print("\n Servner not responding")
        sys.exit()    






