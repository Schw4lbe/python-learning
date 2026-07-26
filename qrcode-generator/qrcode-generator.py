import qrcode

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)


def generate_qrcode():
    clear_console()

    data_list: list = set_data_list()
    colors: list = set_colors()

    if len(colors) == 2:
        img = qr.make_image(fill_color=colors[0], back_color=colors[1])
    else:
        img = qr.make_image(fill_color="black", back_color="white")

    for item in data_list:
        qr.add_data(item[0])
        img.save(f"{item[1]}.png")


def set_data_list():
    data_list: list = []
    while True:
        data: str = get_data_string()
        name: str = get_name_string()

        next_item: str = input("add another item? (y/n): ")
        if next_item == "y":
            data_list.append([data, name])
            continue
        elif next_item == "n":
            data_list.append([data, name])
            return data_list


def get_data_string():
    return input("enter link or text:")


def get_name_string():
    return input("enter file name:")


def set_colors():
    if set_default_overwrite():
        fill_color: tuple = set_color_by_value("FILL COLOR")
        back_color: tuple = set_color_by_value("BACKGROUND COLOR")
        return [fill_color, back_color]
    else:
        return []


def set_default_overwrite():
    is_overwrite: bool = bool(int(input("0 = default colors // 1 = custom: ")))
    if is_overwrite:
        return True
    elif not is_overwrite:
        return False
    else:
        set_default_overwrite
        return


def set_color_by_value(str):
    print(f"ENTER {str}")
    red: int = int(input("0 - 255 for color RED: "))
    green: int = int(input("0 - 255 for color GREEN: "))
    blue: int = int(input("0 - 255 for color BLUE: "))
    return (red, green, blue)


def clear_console():
    # \033[2J → clear the terminal screen
    # \033[H → move cursor to the top-left
    # end="" → don't add another newline
    print("\033[2J\033[H", end="")


def main():
    generate_qrcode()


if __name__ == "__main__":
    main()
