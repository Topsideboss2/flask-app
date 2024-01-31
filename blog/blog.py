from flask import Blueprint, render_template, redirect, url_for

blog = Blueprint("blog", __name__, static_folder="static", template_folder="templates")

@blog.route("/")
def blog_home_page():
    return render_template("generic.html")

@blog.route("/error")
def error():
    return render_template("404.html")

@blog.route("/<name>")
def blog_page(name):
    # Add each blog post here
    if name == "effortlessly-sync-your-files-with-rsync":
        return render_template("blog/rsync.html")
    elif name == "deploying-a-dynamic-website-on-aws-using-a-3-tier-architecture":
        return render_template("blog/tta.html")
    elif name == "how-to-configure-lets-encrypt-ssl-on-ubuntu-20-04":
        return render_template("blog/letsencrypt.html")
    elif name == "deploying-zabbix-on-your-application-server-for-monitoring":
        return render_template("blog/zabbix.html")
    elif name == "what-happens-when-you-type-google-in-your-browser-and-press-enter":
        return render_template("blog/google.html")
    elif name == "aws-cloud-project-bootcamp-week-1":
        return render_template("blog/week1.html")
    elif name == "aws-cloud-project-bootcamp-week-2":
        return render_template("blog/week2.html")
    elif name == "what-is-the-cloud-resume-challenge":
        return render_template("blog/cloudresume.html")
    elif name == "cloud-resume-challenge-conceptual-design":
        return render_template("blog/condiagram.html")
    elif name == "cloud-resume-challenge-setting-up-website-with-html-css-javascript":
        return render_template("blog/website.html")
    elif name == "cloud-resume-challenge-setting-up-s3-bucket":
        return render_template("blog/s3.html")
    elif name == "cloud-resume-challenge-setting-up-cloudfront":
        return render_template("blog/cloudfront.html")
    elif name == "cloud-resume-challenge-setting-up-dynamodb":
        return render_template("blog/dynamodb.html")
    elif name == "cloud-resume-challenge-setting-up-aws-lambda-function":
        return render_template("blog/lambda.html")
    elif name == "cloud-resume-challenge-setting-up-ci-cd-with-github-actions":
        return render_template("blog/cicd.html")
    elif name == "cloud-resume-challenge-implementing-infrastructure-as-code-with-terraform":
        return render_template("blog/terraform.html")
    elif name == "cloud-resume-challenge-implementing-monitoring-with-datadog":
        return render_template("blog/datadog.html")
    else:
        # Add 404 page here
        return redirect(url_for("error"))