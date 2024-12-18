import random as r
import time as t

number="1234567890"
symbol="!@#$%^&*()_+-={}[]|\\:;\"\'<>?"
lower="abcdefghijklmnopqrstuvwxyz"
upper=lower.upper()

def gen(pass_len):
	password = "".join(r.sample(number+symbol+lower+upper,pass_len))
	return password

def main():
	j=int(input("Enter how many Passwords do you need: "))
	pass_len=int(input("Enter the Lenght of the Password: "))
	for i in range(0,j,1):
		print(gen(pass_len)+"\n")
		t.sleep(0.12)

main()