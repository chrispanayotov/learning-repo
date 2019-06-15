def cash_receipt():
    print("CASH RECEIPT")


def dashes():
    print("-" * 30)


def body():
    print("Charged to____________________")
    print("Received by___________________")


def softuni():
    print("© SoftUni")


def print_receipt():
    cash_receipt()
    dashes()
    body()
    dashes()
    softuni()


if __name__ == "__main__":
    print_receipt()