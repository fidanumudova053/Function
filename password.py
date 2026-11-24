def check_password(password):
    errors = []
    if len(password) > 8 :
        errors.append("en az 8 simvol olmalidir")
    if not any(char.isupper() for char in password):
        errors.append(" en azi 1 boyuk herf olmalidir")
    if not any(char.islower() for char in password):
        errors.append("en azi 1 balaca herf olmalidir")
    if not any(char.isdigit() for char in password):
        errors.append("en azi 1 reqem olamlidir")
    if " " in password:
        errors.append("bosluq olmamalidir")
    return errors
for x  in range(3):
    password = input("sifre daxil edin: ")
    errors = check_password(password)
    if not errors:
        print("Şifrə qəbul olundu")
        break
    else:
        for error in errors:
            print(error)
else:
    print("Cəhdlər bitdi")
