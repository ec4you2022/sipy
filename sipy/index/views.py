from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Ourteam, Contact, Blog
from django.conf import settings

def index(request):
    ourteam = Ourteam.objects.all()
    blog = Blog.objects.all()

    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email", None)
        phone = request.POST.get("phone")
        message = request.POST.get("message", "")

        # Save the contact information
        Contact.objects.create(name=name, email=email, phone=phone, message=message)

        # Render email content using an HTML template
        subject = "New Contact Form Submission"
        context = {
            'name': name,
            'email': email,
            'phone': phone,
            'message': message,
        }
        email_body = render_to_string('contact_email.html', context)

        to_email = settings.EMAIL_HOST_USER  # Replace with your email address
        from_email = settings.ADMIN_EMAIL  # Replace with a valid from address
        
        try:
            email_message = EmailMessage(subject, email_body, from_email, [to_email])
            email_message.content_subtype = 'html'  # Set the email content to HTML
            email_message.send()
            messages.success(request, "Your message has been submitted successfully!")
        except Exception as e:
            messages.error(request, f"An error occurred while sending the email: {e}")

        return redirect("index")

    context = {
        'ourteam': ourteam,
        'blog': blog,
    }
    
    return render(request, 'index.html', context)


def blog (request, slug):
    blog = Blog.objects.get(slug=slug)
    all_blogs = Blog.objects.exclude(id=blog.id)[:3]

    return render(request, 'blog.html', {'blog': blog, 'all_blogs': all_blogs})
