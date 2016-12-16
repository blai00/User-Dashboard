from django.shortcuts import render,redirect
from models import User, Message, Comment
# Create your views here.
def index(request):
	return render(request, 'dashboard/index.html')

def login(request):
	result = User.UserManager.login(request)

	if result[0] == False:
		print_messages(request,result[1])
		return redirect('/signin')
	return log_user_in(request, result[1])

def register(request):
	result = User.UserManager.register(request)
	if result[0] == False:
		print_messages(request, result[1])
		return render ('/new')
	return log_user_in(request,result[1])

def dashboard(request):
	user = Users.UserManager.all()
	context = {
		'user' : user
	}
	if not 'user' in request.session:
		return redirect('/login')
	return render(request,'dashboard/dashboard.html', context)

def print_messages(request, message_list):
	for message in message_list:
		messages.add_message(request, messages.INFO, message)

def log_user_in(request, user):
	request.session['user'] = {
	'id' :user.id,
	'first_name':user.first_name,
	'last_name' :user.last_name,
	'email' : user.email
	}

	return redirect('/dashboard')

def logout(request):
	request.session.pop('user')
	return redirect('/login')

def message(request,id):
	user = Message.objects.get(id=id)
	message.objects.create(request.POST['message'])
	
	return redirect('/show')

def comments(request,id):
	user = Comment.objets.get(id=id)
	message = Comment.objects.get(id=id)
	comment.objects.create(request.POST['comment'])
	return redirect('/show')

def show(request):
	user = User.UserManager.all()
	message = Message.objects.all()
	comment = Comment.objects.all()
	context = {
		'user' :user,
		'message' : message,
		'comment' : comment
	}

	return render(request, 'dashbaord/show.html', context)

def update(request,id):
	User.UserManager.update(id)
	return redirect('/')

def delete_message(request,id):
	remove = Message.objets.get(id = id)
	remove.delete()
	return redirect('/show')

def delete_comment(request,id):
	remove = Comment.objects.get(id = id)
	remove.delete()
	return redirect('/show')