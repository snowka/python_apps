
class Character:
    """
    Data for TEI-structured lists of characters in a play
    Attributes:
        Role(string)
        xmlid(string)
        abb_name(string)
        roledesc(string)
    """
    def __init__(self, role, xmlid = "None", abb_name = "None Provided", roledesc = "None Provided"):
        self.role = role
        self.xmlid = xmlid
        self.abb_name = abb_name
        self.roledesc = roledesc

    @classmethod
    def get_user_input(self):
        while 1:
            try:
                role = input("Enter the name of the character from the play: ")
                xmlid = input("Enter the xml:id for your character: ")
                abb_name = input("Enter the abbreviated character name used in the lines of the play: ")
                roledesc = input("Enter the description of the character role: ")
                return self(role, xmlid, abb_name, roledesc)
            except:
                print("Invalid input!")
                continue


def input_sequence():
    char_list.append(Character.get_user_input())
    print(char_list)


def user_query():
    proceed = input("Add character to list of dramatis personae? Y/N: ")
    if proceed == "Y":
        input_sequence()
        user_query()
    elif proceed == "y":
        input_sequence()
        user_query()
    else:
        print("Done adding characters.")

def print_xml(list):
    for i in list:
        print(f"""<castItem>
<role><name type ="role" xml:id = "{i.xmlid}">{i.role}</name></role>
<roleDesc>{i.roledesc}</roleDesc>\n</castItem>
    """)


char_list = []
print("""\nThis tool will collect the information to create your list of dramatis personae.
""")
user_query()
print(char_list)
final_xml = print_xml(char_list)
print(final_xml)
