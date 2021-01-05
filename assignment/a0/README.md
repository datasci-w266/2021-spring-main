# Assignment 0:  Hello W266!

This assignment is a quick walk-through to help you get set up logistically for the course.  It isn't a real assignment and doesn't count towards your grade (but you can't do the other assignments without it!).

**Reminder:** You may only use 2 late days for any one deliverable in this course.  See the [syllabus](../../syllabus/) for details.

If you haven't yet, please:

- Sign up for [Piazza](https://piazza.com/berkeley/spring2021/datasciw266)

Now we'll get you all set up with the software packages and the course GitHub.

1. [Setup](https://calmail.berkeley.edu/manage/account/create_account) a @berkeley.edu account setup if you don't already have one (@ischool.berkeley.edu is insufficient!)

1. **Set up your computing environment:** We recommend using a Google Cloud Compute instance. We have $50 of credits available per student, and it should only take a few minutes to set up by following [our Cloud guide](cloud/).  
If you prefer to work on your own laptop/desktop/server (including AWS), we strongly recommend looking through the cloud setup script and matching versions as closely as possible.
*(Note that due to the variety of systems out there, we can only provide official support for Google Cloud instances.)*

2. **Clone the course repo** (if you didn't already in the Cloud guide) with:  
`git clone https://github.com/datasci-w266/2021-spring-main.git ~/w266`  
You may also want to do this on your laptop to have a local copy.  

3. **Answer the questions in the `answers`** file in the `assignment/a0`directory.  (If you wish, you can run the presubmit script, answers\_test.py, yourself.  The submit script below will also run these before it pushes.  Unlike in future assignments, these presubmits check your answers for you.)
Commit the change with `git commit`.

4. **Open and run `a0.ipynb`**. This notebook will check that your Python packages are up-to-date, test TensorFlow, and give a taste of some of the NLP datasets we'll be working with. You don't need to write any code here - just run the cells, save, and commit the updated notebook to git.  `git commit` the resulting populated notebook so that we know you ran it.

4. **Create your personal submission repo** at [this link](https://classroom.github.com/a/D8L0msR9). We'll use this for submitting assignments; it's private to you and the instructors.

5. **Run the submit script**: `./assignment/submit.sh -u your-github-username -a 0`, which will push to your personal repo. It will try to verify the submission, but you can should also visit the repo on GitHub and confirm that your changes show up.  (For all assignments in this course, it's your responsibility to make sure your submission has made it to GitHub!)  **Note:** There is no need to send pull requests or any of the other usual git machinery.  All you need to do is run the submit script and check that your code appeared in a branch named a0-submit in your "classroom" repository you setup in the previous step.  If you can't find it, **this is a problem**.  If you can't figure it out, ask (preferably publicly) on Piazza and someone will help you out.  There will be a small number of points for each assignment for submitting your homework in the right place.

## Next...

Continue on to [Assignment 1](../a1/) once it's released.  (Unlike Assignment 0, Assignment 1 isn't just a setup exercise.  Don't wait too long to get started!)
