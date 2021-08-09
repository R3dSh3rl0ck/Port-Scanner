# Port-Scanner in Python

# Main!
*Program execution : -Define the target/s (IPv4 or domain-TLD name). 
                     -Define Port range (1-65535).
                     - Executon via terminal python3 Pscanner.py
                     -Execytion via CMD python Pscanner.py
                    
# Genereal Inforamtios!
*The program uses threading programming for speed.Concretely a threadpoolexecutor (max workers = 100..Change the number to your needs maybe is great enough).
*For the IPy library --> Use a terminal | Cmd and type(command) --> pip3 install IPy(if you don not have pip installed --> sudo apt install python3-pip (Debian)
                                                                --> pip install IPy                                    --> python get-pip.py (Windows)
                                                                                                         -curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
                                                                                                         -python3 get-pip.py (macOS)
* The code includes helpfull comments for your undestanding.
* The Project Includes a port.txt file with the common communication ports,where you can find and see which protocol or service uses the specific port,you can add more from your researches!
