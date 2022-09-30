# def octant_transition_count(mod=5000):
# ###Code

# from platform import python_version
# ver = python_version()

# if ver == "3.8.10":
#     print("Correct Version Installed")
# else:
#     print("Please install 3.8.10. Instruction are present in the GitHub Repo/Webmail. Url: https://pastebin.com/nvibxmjw")

# mod=5000
# octant_transition_count(mod)


###### defining mod value
mod=5000

##### importing openpyxl and nan and loading workbook
try:
    from cmath import nan
    import openpyxl

    wb = openpyxl.load_workbook(r'C:\Users\DELL\OneDrive\Desktop\temp_octant\input_octant_transition_identify - Copy.xlsx')
except:
    print("there is error in loading workbook check your file directory and import openpyxl")
    exit()
