from django.shortcuts import render, redirect
from .models import President, UserProfile, Vice_President, General_Secretary, Financial_Secretary, Social_Director, Technical_Director, Sports_Director, Public_Relations_Officer, Treasurer, Welfare_Director,assistant_general_secretary, assistant_social_director, P_R_O1, P_R_O2, UserVote
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages



def index(request):
    return render(request, 'index.html')

def close(request):
    return render(request, 'close.html')

def next_page(request):
    return render(request, 'next_page.html')


def election_results(request):
    president_votes = President.objects.values_list('name', 'votes')
    vice_president_votes = Vice_President.objects.values_list('name', 'votes')
    general_secretary_votes = General_Secretary.objects.values_list('name', 'votes')
    financial_secretary_votes = Financial_Secretary.objects.values_list('name', 'votes')
    social_director_votes = Social_Director.objects.values_list('name', 'votes')
    technical_director_votes = Technical_Director.objects.values_list('name', 'votes')
    sports_director_votes = Sports_Director.objects.values_list('name', 'votes')
    public_relations_officer_votes = Public_Relations_Officer.objects.values_list('name', 'votes')
    treasurer_votes = Treasurer.objects.values_list('name', 'votes')
    welfare_director_votes = Welfare_Director.objects.values_list('name', 'votes')
    assistant_general_secretary_votes = assistant_general_secretary.objects.values_list('name', 'votes')
    assistant_social_director_votes = assistant_social_director.objects.values_list('name', 'votes')
    pro1_votes = P_R_O1.objects.values_list('name', 'votes')
    pro2_votes = P_R_O2.objects.values_list('name', 'votes')

    # Prepare data for the pie charts
    labels = [candidate[0] for candidate in president_votes]
    votes = [candidate[1] for candidate in president_votes]

    vlabels = [candidate[0] for candidate in vice_president_votes]
    vvotes = [candidate[1] for candidate in vice_president_votes]

    gs_labels = [candidate[0] for candidate in general_secretary_votes]
    gs_votes = [candidate[1] for candidate in general_secretary_votes]

    fs_labels = [candidate[0] for candidate in financial_secretary_votes]
    fs_votes = [candidate[1] for candidate in financial_secretary_votes]

    sd_labels = [candidate[0] for candidate in social_director_votes]
    sd_votes = [candidate[1] for candidate in social_director_votes]

    td_labels = [candidate[0] for candidate in technical_director_votes]
    td_votes = [candidate[1] for candidate in technical_director_votes]

    sp_labels = [candidate[0] for candidate in sports_director_votes]
    sp_votes = [candidate[1] for candidate in sports_director_votes]

    pro_labels = [candidate[0] for candidate in public_relations_officer_votes]
    pro_votes = [candidate[1] for candidate in public_relations_officer_votes]

    t_labels = [candidate[0] for candidate in treasurer_votes]
    t_votes = [candidate[1] for candidate in treasurer_votes]

    wd_labels = [candidate[0] for candidate in welfare_director_votes]
    wd_votes = [candidate[1] for candidate in welfare_director_votes]

    as_labels = [candidate[0] for candidate in assistant_general_secretary_votes]
    as_votes = [candidate[1] for candidate in assistant_general_secretary_votes]

    assd_labels = [candidate[0] for candidate in assistant_social_director_votes]
    assd_votes = [candidate[1] for candidate in assistant_social_director_votes]

    p1_labels = [candidate[0] for candidate in pro1_votes]
    p1_votes = [candidate[1] for candidate in pro1_votes]

    p2_labels = [candidate[0] for candidate in pro2_votes]
    p2_votes = [candidate[1] for candidate in pro2_votes]

    context = {
        'labels': labels,
        'votes': votes,
        'vlabels': vlabels,
        'vvotes': vvotes,
        'gs_labels': gs_labels,
        'gs_votes': gs_votes,
        'fs_labels': fs_labels,
        'fs_votes': fs_votes,
        'sd_labels': sd_labels,
        'sd_votes': sd_votes,
        'td_labels': td_labels,
        'td_votes': td_votes,
        'sp_labels': sp_labels,
        'sp_votes': sp_votes,
        'pro_labels': pro_labels,
        'pro_votes': pro_votes,
        't_labels': t_labels,
        't_votes': t_votes,
        'wd_labels': wd_labels,
        'wd_votes': wd_votes,
        'as_labels': as_labels,
        'as_votes': as_votes,
        'assd_labels': assd_labels,
        'assd_votes': assd_votes,
        'p1_labels': p1_labels,
        'p1_votes': p1_votes,
        'p2_labels': p2_labels,
        'p2_votes': p2_votes,
    }
    return render(request, 'election_results.html', context)

def vote(request):
    presidents = President.objects.all()
    vice_presidents = Vice_President.objects.all()
    general_secretaries = General_Secretary.objects.all()
    welfare_directors = Welfare_Director.objects.all()
    financial_secretaries = Financial_Secretary.objects.all()
    social_directors = Social_Director.objects.all()
    technical_directors = Technical_Director.objects.all()
    sports_directors = Sports_Director.objects.all()
    public_relations_officers = Public_Relations_Officer.objects.all()
    treasurers = Treasurer.objects.all()
    pro1s = P_R_O1.objects.all()
    pro2s = P_R_O2.objects.all()
    assistant_general_secretaries = assistant_general_secretary.objects.all()
    assistant_social_directors = assistant_social_director.objects.all()

    # Render the template with candidates for each position
    return render(request, 'vote.html', {
        'presidents': presidents,
        'vice_presidents': vice_presidents,
        'general_secretaries': general_secretaries,
        'welfare_directors': welfare_directors,
        'financial_secretaries': financial_secretaries,
        'social_directors': social_directors,
        'technical_directors': technical_directors,
        'sports_directors': sports_directors,
        'public_relations_officers': public_relations_officers,
        'treasurers': treasurers,
        'pro1s': pro1s,
        'pro2s': pro2s,
        'assistant_general_secretaries': assistant_general_secretaries,
        'assistant_social_directors': assistant_social_directors,
    })


def login_view(request):
    if request.method == 'POST':
        matric_number = request.POST.get('matric_number', '').strip().lower()  # Convert to lowercase

        # Debugging: Print the matric number
        print("Matric Number:", matric_number)

        # Validate matric number format
        if not re.match(r'^[a-z]{2}\d{6}-\d{4}$', matric_number):
            feedback_message = "Invalid matric number format."
            return render(request, 'next_page.html', {'feedback_message': feedback_message})

        # Extract year, department, and last 4 digits from matric number
        year = int(matric_number[2:5])
        department = int(matric_number[5:8])
        last_four_digits = int(matric_number[-4:])

        # Check if year and department are valid
        if year not in [190, 200, 210, 220, 230] or department not in [301, 302, 303, 304, 305, 306, 307]:
            feedback_message = "Invalid year or department in matric number."
            return render(request, 'next_page.html', {'feedback_message': feedback_message})

        # Check if the last 4 digits are in the range [1993, 9999]
        if last_four_digits < 1993 or last_four_digits > 9999:
            feedback_message = "Invalid last 4 digits in matric number."
            return render(request, 'next_page.html', {'feedback_message': feedback_message})

        email = request.POST.get('email', '').strip().lower()  # Convert email to lowercase

        # Validate email format
        if not re.match(r'^[a-zA-Z0-9._%+-]+@elizadeuniversity\.edu\.ng$', email):
            feedback_message = "Invalid email format. Please use an @elizadeuniversity.edu.ng email."
            return render(request, 'next_page.html', {'feedback_message': feedback_message})

        # Set the matric_number and email in the session
        request.session['matric_number'] = matric_number
        request.session['email'] = email

        # Save the matric_number and email to the UserProfile model
        user_profile, created = UserProfile.objects.get_or_create(matric_number=matric_number, defaults={'email': email, 'has_voted': False})

        # Check if the user has already voted
        if user_profile.has_voted:
            return redirect('close')  # Redirect to the end page if the user has already voted

        # Redirect to the voting page
        return redirect('vote')

    return render(request, 'next_page.html')





def vote_submit(request):
    if request.method == 'POST':
        # Get the selected candidates' IDs from the submitted form
        president_id = request.POST.get('president')
        vice_president_id = request.POST.get('vice_president')
        general_secretary_id = request.POST.get('general_secretaries')
        welfare_director_id = request.POST.get('welfare_director')
        financial_secretary_id = request.POST.get('financial_secretary')
        social_director_id = request.POST.get('social_director')
        technical_director_id = request.POST.get('technical_director')
        sports_director_id = request.POST.get('sports_director')
        public_relations_officer_id = request.POST.get('public_relations_officer')
        treasurer_id = request.POST.get('treasurer')
        PRO1id = request.POST.get('pro1')
        PRO2id = request.POST.get('pro2')
        assistant_general_secretary_id = request.POST.get('assistant_general_secretary')
        assistant_social_director_id = request.POST.get('assistant_social_director')

        # Check if any position was left unvoted (you may want to customize this part)

        if not president_id or not vice_president_id or not general_secretary_id \
                or not welfare_director_id or not financial_secretary_id \
                or not social_director_id or not technical_director_id \
                or not sports_director_id or not public_relations_officer_id \
                or not treasurer_id or not assistant_general_secretary_id \
                or not assistant_social_director_id or not PRO1id or not PRO2id:
            return redirect('vote')

        # Record the votes in your models (you may want to handle this based on your models)
        president = President.objects.get(pk=president_id)
        president.votes += 1
        president.save()

        vice_president = Vice_President.objects.get(pk=vice_president_id)
        vice_president.votes += 1
        vice_president.save()

        general_secretary = General_Secretary.objects.get(pk=general_secretary_id)
        general_secretary.votes += 1
        general_secretary.save()

        welfare_director = Welfare_Director.objects.get(pk=welfare_director_id)
        welfare_director.votes += 1
        welfare_director.save()

        financial_secretary = Financial_Secretary.objects.get(pk=financial_secretary_id)
        financial_secretary.votes += 1
        financial_secretary.save()

        social_director = Social_Director.objects.get(pk=social_director_id)
        social_director.votes += 1
        social_director.save()

        technical_director = Technical_Director.objects.get(pk=technical_director_id)
        technical_director.votes += 1
        technical_director.save()

        sports_director = Sports_Director.objects.get(pk=sports_director_id)
        sports_director.votes += 1
        sports_director.save()

        public_relations_officer = Public_Relations_Officer.objects.get(pk=public_relations_officer_id)
        public_relations_officer.votes += 1
        public_relations_officer.save()

        treasurer = Treasurer.objects.get(pk=treasurer_id)
        treasurer.votes += 1
        treasurer.save()

        PRO1 = P_R_O1.objects.get(pk=PRO1id)
        PRO1.votes += 1
        PRO1.save()

        PRO2 = P_R_O2.objects.get(pk=PRO2id)
        PRO2.votes += 1
        PRO2.save()

        assistantgeneralsecretary = assistant_general_secretary.objects.get(pk=assistant_general_secretary_id)
        assistantgeneralsecretary.votes += 1
        assistantgeneralsecretary.save()

        assistantsocialdirector  = assistant_social_director.objects.get(pk=assistant_social_director_id)
        assistantsocialdirector.votes += 1
        assistantsocialdirector.save()

        user_profile = UserProfile.objects.get(matric_number=request.session.get('matric_number'))
        UserVote.objects.create(
            user_profile=user_profile,
            email=user_profile.email,  # Assign the user's email
            president_voted=president,
            vice_president_voted=vice_president,
            general_secretary_voted=general_secretary,
            financial_secretary_voted=financial_secretary,
            social_director_voted=social_director,
            technical_director_voted=technical_director,
            sports_director_voted=sports_director,
            public_relations_officer_voted=public_relations_officer,
            treasurer_voted=treasurer,
            welfare_director_voted=welfare_director,
            assistant_general_secretary_voted=assistantgeneralsecretary,
            assistant_social_director_voted=assistantsocialdirector,
            pro1_voted=PRO1,
            pro2_voted=PRO2
        )
        user_profile.has_voted = True
        user_profile.save()
        
        return render(request, 'close.html')

        # Mark the user as voted in the UserProfile
        #president_candidates = President.objects.values('name', 'votes')
        #vice_president_candidates = Vice_President.objects.values('name', 'votes')
        #general_secretary_candidates = General_Secretary.objects.values('name', 'votes')
        #welfare_director_candidates = Welfare_Director.objects.values('name', 'votes')
        #financial_secretary_candidates = Financial_Secretary.objects.values('name', 'votes')
        #social_director_candidates = Social_Director.objects.values('name', 'votes')
        #technical_director_candidates = Technical_Director.objects.values('name', 'votes')
        #sports_director_candidates = Sports_Director.objects.values('name', 'votes')
        #public_relations_officer_candidates = Public_Relations_Officer.objects.values('name', 'votes')
        #treasurer_candidates = Treasurer.objects.values('name', 'votes')
        #assistant_general_secretary_candidates = assistant_general_secretary.objects.values('name', 'votes')
        #assistant_social_director_candidates = assistant_social_director.objects.values('name', 'votes')
        #pro1_candidates = P_R_O1.objects.values('name', 'votes')
        #pro2_candidates = P_R_O2.objects.values('name', 'votes')

        #return render(request, 'end.html', {
        #   'president_candidates': president_candidates,
        #    'vice_president_candidates': vice_president_candidates,
        #    'general_secretary_candidates': general_secretary_candidates,
        #    'welfare_director_candidates': welfare_director_candidates,
        #    'financial_secretary_candidates': financial_secretary_candidates,
        #    'social_director_candidates': social_director_candidates,
        #    'technical_director_candidates': technical_director_candidates,
        #    'sports_director_candidates': sports_director_candidates,
        #    'public_relations_officer_candidates': public_relations_officer_candidates,
        #    'treasurer_candidates': treasurer_candidates,
        #    'assistant_general_secretary_candidates': assistant_general_secretary_candidates,
        #    'assistant_social_director_candidates': assistant_social_director_candidates,
        #    'pro1_candidates': pro1_candidates,
        #    'pro2_candidates': pro2_candidates,
        #})
    
        
    # If the request method is not POST, handle it accordingly (redirect or render a different page)
    return redirect('close')  

def end(request):
        president_candidates = President.objects.values('name', 'votes')
        vice_president_candidates = Vice_President.objects.values('name', 'votes')
        general_secretary_candidates = General_Secretary.objects.values('name', 'votes')
        welfare_director_candidates = Welfare_Director.objects.values('name', 'votes')
        financial_secretary_candidates = Financial_Secretary.objects.values('name', 'votes')
        social_director_candidates = Social_Director.objects.values('name', 'votes')
        technical_director_candidates = Technical_Director.objects.values('name', 'votes')
        sports_director_candidates = Sports_Director.objects.values('name', 'votes')
        public_relations_officer_candidates = Public_Relations_Officer.objects.values('name', 'votes')
        treasurer_candidates = Treasurer.objects.values('name', 'votes')
        assistant_general_secretary_candidates = assistant_general_secretary.objects.values('name', 'votes')
        assistant_social_director_candidates = assistant_social_director.objects.values('name', 'votes')
        pro1_candidates = P_R_O1.objects.values('name', 'votes')
        pro2_candidates = P_R_O2.objects.values('name', 'votes')

        return render(request, 'end.html', {
            'president_candidates': president_candidates,
            'vice_president_candidates': vice_president_candidates,
            'general_secretary_candidates': general_secretary_candidates,
            'welfare_director_candidates': welfare_director_candidates,
            'financial_secretary_candidates': financial_secretary_candidates,
            'social_director_candidates': social_director_candidates,
            'technical_director_candidates': technical_director_candidates,
            'sports_director_candidates': sports_director_candidates,
            'public_relations_officer_candidates': public_relations_officer_candidates,
            'treasurer_candidates': treasurer_candidates,
            'assistant_general_secretary_candidates': assistant_general_secretary_candidates,
            'assistant_social_director_candidates': assistant_social_director_candidates,
            'pro1_candidates': pro1_candidates,
            'pro2_candidates': pro2_candidates,
        })

#update
def upload(request):
    if request.method == 'POST':
        # Process form data here
        president_name = request.POST.get('president_name')
        president_picture = request.FILES.get('president_picture')
        president_department = request.POST.get('president_department')
        president_level = request.POST.get('president_level')
        president_votes = request.POST.get('president_votes')
        president = President.objects.create(name=president_name, picture=president_picture, department=president_department, level=president_level, votes=president_votes)

        vice_president_name = request.POST.get('vice_president_name')
        vice_president_picture = request.FILES.get('vice_president_picture')
        vice_president_department = request.POST.get('vice_president_department')
        vice_president_level = request.POST.get('vice_president_level')
        vice_president_votes = request.POST.get('vice_president_votes')
        vice_president = Vice_President.objects.create(name=vice_president_name, picture=vice_president_picture, department=vice_president_department, level=vice_president_level, votes=vice_president_votes)

        general_secretary_name = request.POST.get('general_secretary_name')
        general_secretary_picture = request.FILES.get('general_secretary_picture')
        general_secretary_department = request.POST.get('general_secretary_department')
        general_secretary_level = request.POST.get('general_secretary_level')
        general_secretary_votes = request.POST.get('general_secretary_votes')
        general_secretary = General_Secretary.objects.create(name=general_secretary_name, picture=general_secretary_picture, department=general_secretary_department, level=general_secretary_level, votes=general_secretary_votes)

        financial_secretary_name = request.POST.get('financial_secretary_name')
        financial_secretary_picture = request.FILES.get('financial_secretary_picture')
        financial_secretary_department = request.POST.get('financial_secretary_department')
        financial_secretary_level = request.POST.get('financial_secretary_level')
        financial_secretary_votes = request.POST.get('financial_secretary_votes')
        financial_secretary = Financial_Secretary.objects.create(name=financial_secretary_name, picture=financial_secretary_picture, department=financial_secretary_department, level=financial_secretary_level, votes=financial_secretary_votes)

        social_director_name = request.POST.get('social_director_name')
        social_director_picture = request.FILES.get('social_director_picture')
        social_director_department = request.POST.get('social_director_department')
        social_director_level = request.POST.get('social_director_level')
        social_director_votes = request.POST.get('social_director_votes')
        social_director = Social_Director.objects.create(name=social_director_name, picture=social_director_picture, department=social_director_department, level=social_director_level, votes=social_director_votes)

        technical_director_name = request.POST.get('technical_director_name')
        technical_director_picture = request.FILES.get('technical_director_picture')
        technical_director_department = request.POST.get('technical_director_department')
        technical_director_level = request.POST.get('technical_director_level')
        technical_director_votes = request.POST.get('technical_director_votes')
        technical_director = Technical_Director.objects.create(name=technical_director_name, picture=technical_director_picture, department=technical_director_department, level=technical_director_level, votes=technical_director_votes)

        sports_director_name = request.POST.get('sports_director_name')
        sports_director_picture = request.FILES.get('sports_director_picture')
        sports_director_department = request.POST.get('sports_director_department')
        sports_director_level = request.POST.get('sports_director_level')
        sports_director_votes = request.POST.get('sports_director_votes')
        sports_director = Sports_Director.objects.create(name=sports_director_name, picture=sports_director_picture, department=sports_director_department, level=sports_director_level, votes=sports_director_votes)


        treasurer_name = request.POST.get('treasurer_name')
        treasurer_picture = request.FILES.get('treasurer_picture')
        treasurer_department = request.POST.get('treasurer_department')
        treasurer_level = request.POST.get('treasurer_level')
        treasurer_votes = request.POST.get('treasurer_votes')
        treasurer = Treasurer.objects.create(name=treasurer_name, picture=treasurer_picture, department=treasurer_department, level=treasurer_level, votes=treasurer_votes)

        welfare_director_name = request.POST.get('welfare_director_name')
        welfare_director_picture = request.FILES.get('welfare_director_picture')
        welfare_director_department = request.POST.get('welfare_director_department')
        welfare_director_level = request.POST.get('welfare_director_level')
        welfare_director_votes = request.POST.get('welfare_director_votes')
        welfare_director = Welfare_Director.objects.create(name=welfare_director_name, picture=welfare_director_picture, department=welfare_director_department, level=welfare_director_level, votes=welfare_director_votes)

        assistant_general_secretary_name = request.POST.get('assistant_general_secretary_name')
        assistant_general_secretary_picture = request.FILES.get('assistant_general_secretary_picture')
        assistant_general_secretary_department = request.POST.get('assistant_general_secretary_department')
        assistant_general_secretary_level = request.POST.get('assistant_general_secretary_level')
        assistant_general_secretary_votes = request.POST.get('assistant_general_secretary_votes')
        assistant_general_secretarys = assistant_general_secretary.objects.create(name=assistant_general_secretary_name, picture=assistant_general_secretary_picture, department=assistant_general_secretary_department, level=assistant_general_secretary_level, votes=assistant_general_secretary_votes)

        assistant_social_director_name = request.POST.get('assistant_social_director_name')
        assistant_social_director_picture = request.FILES.get('assistant_social_director_picture')
        assistant_social_director_department = request.POST.get('assistant_social_director_department')
        assistant_social_director_level = request.POST.get('assistant_social_director_level')
        assistant_social_director_votes = request.POST.get('assistant_social_director_votes')
        assistant_social_directors = assistant_social_director.objects.create(name=assistant_social_director_name, picture=assistant_social_director_picture, department=assistant_social_director_department, level=assistant_social_director_level, votes=assistant_social_director_votes)

        P_R_O1_name = request.POST.get('pro1_name')
        P_R_O1_picture = request.FILES.get('pro1_picture')
        P_R_O1_department = request.POST.get('pro1_department')
        P_R_O1_level = request.POST.get('pro1_level')
        P_R_O1_votes = request.POST.get('pro1_votes')
        P_R_O1s = P_R_O1.objects.create(name=P_R_O1_name, picture=P_R_O1_picture, department=P_R_O1_department, level=P_R_O1_level, votes=P_R_O1_votes)

        P_R_O2_name = request.POST.get('pro2_name')
        P_R_O2_picture = request.FILES.get('pro2_picture')
        P_R_O2_department = request.POST.get('pro2_department')
        P_R_O2_level = request.POST.get('pro2_level')
        P_R_O2_votes = request.POST.get('pro2_votes')
        P_R_O2s = P_R_O2.objects.create(name=P_R_O2_name, picture=P_R_O2_picture, department=P_R_O2_department, level=P_R_O2_level, votes=P_R_O2_votes)

  
        return render(request, 'upload.html', {'success_message': 'Data saved successfully'})
    else:
        return render(request, 'upload.html', {'success_message': 'Data not saved'})
    
#update
def candidate_list(request):
    presidents = President.objects.all()
    vice_presidents = Vice_President.objects.all()
    general_secretaries = General_Secretary.objects.all()
    welfare_directors = Welfare_Director.objects.all()
    financial_secretaries = Financial_Secretary.objects.all()
    social_directors = Social_Director.objects.all()
    technical_directors = Technical_Director.objects.all()
    sports_directors = Sports_Director.objects.all()
    treasurers = Treasurer.objects.all()
    pro1s = P_R_O1.objects.all()
    pro2s = P_R_O2.objects.all()
    assistant_general_secretaries = assistant_general_secretary.objects.all()
    assistant_social_directors = assistant_social_director.objects.all()
        
    return render(request, 'candidate_list.html', {
        'presidents': presidents,
        'vice_presidents': vice_presidents,
        'general_secretaries': general_secretaries,
        'financial_secretaries': financial_secretaries,
        'social_directors': social_directors,
        'technical_directors': technical_directors,
        'sports_directors': sports_directors,
        'treasurers': treasurers,
        'welfare_directors': welfare_directors,
        'assistant_general_secretaries': assistant_general_secretaries,
        'assistant_social_directors': assistant_social_directors,
        'pro1s': pro1s,
        'pro2s': pro2s,
    })

def delete_candidate(request, position, candidate_id):
    # Determine the model based on the position
    model_map = {
        'president': President,
        'user_profile': UserProfile,
        'vice_president': Vice_President,
        'general_secretary': General_Secretary,
        'financial_secretary': Financial_Secretary,
        'social_director': Social_Director,
        'technical_director': Technical_Director,
        'sports_director': Sports_Director,
        'treasurer': Treasurer,
        'welfare_director': Welfare_Director,
        'assistant_general_secretary': assistant_general_secretary,
        'assistant_social_director': assistant_social_director,
        'pro1': P_R_O1,
        'pro2': P_R_O2,
    }
    
    model = model_map.get(position)
    if model:
        try:
            candidate = model.objects.get(pk=candidate_id)
            candidate.delete()
        except model.DoesNotExist:
            pass

    return redirect('candidate_list')


def custom_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('custom_login')  # Redirect to home page after successful sign-up
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('upload')  # Redirect to home page after successful login
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'login.html')
