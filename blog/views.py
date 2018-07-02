from django.shortcuts import render

# Create your views here.
##J: the above two lines are the only ones add by django

## J:Gilrs: a view is a function.
## render=put together
def post_list(request):
	return render(request, 'blog/post_list.html', {})