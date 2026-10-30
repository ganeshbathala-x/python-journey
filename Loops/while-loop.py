secret_num =7

guess_count =0
guess_limit= 3

while guess_count <guess_limit:
	guess= int(input("guess"))
	if guess== secret_num:
		print("you won")
		break;
		
	else:
			print("you failed")
	
