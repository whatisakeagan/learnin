//CONTENT
//biographical & contect information
var bio = {
    "name": "Keagan McPherson",
    "role": " ",
    "contacts": {
        "mobile": "redacted",
        "email": "redacted",
        "github": "whatisakeagan",
        "twitter": "whatisakeagan",
        "location": "Ironwood, MI, US"
    },
    "welcomeMessage": "Expertise in measuring and analyzing human behavior.",
    "skills": ["Data Analysis", "Clinical Research", "R, SPSS, PsychoPy, E-Prime", "SCID-IV, MMPI-2, MRI Basic Operations", "Python, HTML, JavaScript, CSS"],
    "biopic": "images/PatientImage.jpeg"
};

// work experience
var work = {
    "jobs": [{
        "title": "Customer Success",
        "employer": "Expensify",
        "dates": "2015 - present",
        "location": "San Francisco, CA, US",
        "description": "Assisting customers with expense report management software. Independently developed a data capturing, logging, and analysis system for all incoming customer conversations, and used this data to work collaboratively across teams to provide continuing product improvements."
    }, {
        "title": "Assistant Scientist",
        "employer": "University of Minnesota",
        "dates": "2013 - 2014",
        "location": "Minneapolis, MN, US",
        "description": "Chief coordination of a clinical translational science research laboratory with research projects housed in multiple departments (e.g., Academic Health Center, Ophthalmology, Neuroscience, & Psychology). Responsibilities were approximately 40% research (e.g., software/program design, statistical analyses, manuscript writing), 35% clinical (e.g., SCID diagnoses, neuropsychological assessments), and 25% administrative and supervisory (e.g., undergraduate/graduate RA coordination and supervision, patient/participant scheduling, clinic assistant supervision)."
    }, {
        "title": "Research Assistant",
        "employer": "Mayo Clinic",
        "dates": "2012 - 2013",
        "location": "Rochester, MN, US",
        "description": "Work with a multidisciplinary team of clinical health psychologists specializing in cancer, obesity, physical activity, depression and tobacco cessation clinical research. Duties included protocol development and review, manuscript co-authorship, health promotion development and testing, and data collection and analysis."
    }, {
        "title": "Adjunct Professor",
        "employer": "Minnesota State University",
        "dates": "2012 - 2013",
        "location": "Mankato, MN, US",
        "description": "Primary sole instructor for Statistics for Psychology (PSYC201)."
    }, {
        "title": "Assessment Clinician",
        "employer": "Minnesota State Univeristy Psychological Assessment Clinic",
        "dates": "2011 - 2013",
        "location": "Mankato, MN, US",
        "description": "Administration and scoring of standardized diagnostic interviews, the WAIS-IV, WJ-III Tests of Academic Achievement, and TOMM, as well as clinical progress note and final report writing for individuals referred for assessment of learning disabilities, Attention- Deficit/Hyperactivity Disorder and other psychological/behavioral disabilities."
    }, {
        "title": "Graduate Teaching Assistant",
        "employer": "Minnesota State University",
        "dates": "2011 - 2012",
        "location": "Mankato, MN, US",
        "description": "Test proctoring, student coordination, guest lecturing, and other duties as needed for the following courses: Biopsychology (PSY421; AY 2011-12), Drugs & Behavior (PSYC420; Spring 2012), Sensation & Perception (PSYC413; Spring 2012), Research Methods & Design (PSYC211; Spring 2012), Introduction to Psychology (PSYC101Fall 2011)."
    }, {
        "title": "Housing Program Assistant",
        "employer": "The Link",
        "dates": "2010 - 2011",
        "location": "Minneapolis, MN, US",
        "description": "Provided support to disadvantaged, underserved, and/or emotionally/behaviorally disturbed youth in transitional housing related to life, personal, and professional skills necessary to be independently functional."
    }, {
        "title": "Group Home Counselor",
        "employer": "Dependable Home Healthcare",
        "dates": "2010 - 2011",
        "location": "St. Paul, MN, US",
        "description": "Provided care to developmentally delayed adult men—e.g., assisting in personal/social activities, ranging from completing personal hygiene checklists to interacting with individuals in the community—as well as managing of treatment plans, case note maintenance, and medication administration."
    }, {
        "title": "Tutor/Mentor",
        "employer": "AmeriCorps",
        "dates": "2008 - 2010",
        "location": "Minneapolis, MN, US",
        "description": "Private tutoring and academic consulting provided to independent clients (chiefly post-secondary students) in the Minneapolis/St. Paul metro area. Mentored emotionally and behaviorally disturbed, disadvantaged, and underserved children both in- and out-of-classroom. Piloted the first GLBT-oriented after-school program at the K-8 level in Minneapolis Public Schools."
    }, {
        "title": "Peer Tutor",
        "employer": "Gogebic Community College",
        "dates": "2007 - 2008",
        "location": "Ironwood, MI, US",
        "description": "Tutored college students in one-on-one and small group formats in Psychology, Sociology, Mathematics, English, and Biology."
    }]
};

//project information
var projects = {
    "projects": [{
        "title": "Customer Support Quality - Expensify",
        "description": "Created a tagging system to collect, process, and disseminate data about why the quality of the customer experience at Expensify to inform product improvements.",
        "dates": "January 2016 - present",
        "images": ["images/Workbook1.png"]
    }]
};

//education information
var education = {
    "schools": [{
        "name": "Minnesota State University",
        "location": "Mankato, MN, US",
        "degree": "Master of Arts",
        "dates": "2013",
        "majors": ["Clinical Psychology"]
    }, {
        "name": "University of Minnesota",
        "location": "Minneapolis, MN, US",
        "degree": "Bachelor of Arts",
        "dates": "2010",
        "majors": ["Psychology", " GLBT Studies"]
    }, {
        "name": "Gogebic Community College",
        "location": "Ironwood, MI, US",
        "degree": "Associate of Arts",
        "dates": "2008",
        "majors": ["Psychology"]
    }, {
        "name": "MiraCosta College",
        "location": "Oceanside, CA, US",
        "degree": "Associate of Arts",
        "dates": " ",
        "majors": ["Music Production"]
    }],
    "onlineCourses": [{
        "title": "Intro. to Programming Nanodegree",
        "school": "Udacity",
        "dates": "2016",
        "url": "https://www.udacity.com/"
    }]
};

////// DEFINE FUNCTIONS
//// function to display biographical information
bio.display = function() {
    var formattedName = HTMLheaderName.replace("%data%", bio.name);
    var formattedRole = HTMLheaderRole.replace("%data%", bio.role);
    var formattedMessage = HTMLwelcomeMsg.replace("%data%", bio.welcomeMessage);
    var formattedPic = HTMLbiopic.replace("%data%", bio.biopic);
    $("#header").prepend(formattedName, formattedRole, formattedPic, formattedMessage);

    $("#header").append(HTMLskillsStart);
    bio.skills.forEach(function(skill) {
        var formattedSkill = HTMLskills.replace("%data%", skill);
        $("#skills").append(formattedSkill);
    });

    var formattedMobile = HTMLmobile.replace("%data%", bio.contacts.mobile);
    var formattedEmail = HTMLemail.replace("%data%", bio.contacts.email);
    var formattedGH = HTMLgithub.replace("%data%", bio.contacts.github);
    var formattedTwitter = HTMLtwitter.replace("%data%", bio.contacts.twitter);
    var formattedLocation = HTMLlocation.replace("%data%", bio.contacts.location);

    $("#topContacts").append(formattedMobile, formattedEmail, formattedGH, formattedTwitter, formattedLocation);
    $("#footerContacts").append(formattedMobile, formattedEmail, formattedGH, formattedTwitter, formattedLocation);
};

//// function to display education
education.display = function() {
    education.schools.forEach(function(school) {
        // create new div for education experience
        $("#education").append(HTMLschoolStart);
        var formattedSchoolName = HTMLschoolName.replace('%data%', school.name);
        var formattedSchoolCity = HTMLschoolLocation.replace("%data%", school.location);
        var formattedSchoolNameCity = formattedSchoolName + formattedSchoolCity;
        $(".education-entry:last").append(formattedSchoolNameCity);

        var formattedDegree = HTMLschoolDegree.replace("%data%", school.degree);
        $(".education-entry:last").append(formattedDegree);

        var formattedMajor = HTMLschoolMajor.replace("%data%", school.majors);
        $(".education-entry:last").append(formattedMajor);

        var formattedGrad = HTMLschoolDates.replace("%data%", school.dates);
        $(".education-entry:last").append(formattedGrad);
    });
    $("#education").append(HTMLonlineClasses);
    for (var course in education.onlineCourses) {
        $("#education").append(HTMLschoolStart);
        var formattedOnlineTitle = HTMLonlineTitle.replace("%data%", education.onlineCourses[course].title);
        $(".education-entry:last").append(formattedOnlineTitle);

        var formattedOnlineSchool = HTMLonlineSchool.replace("%data%", education.onlineCourses[course].school);
        $(".education-entry:last").append(formattedOnlineSchool);

        var formattedOnlineDates = HTMLonlineDates.replace("%data%", education.onlineCourses[course].dates);
        $(".education-entry:last").append(formattedOnlineDates);

        var formattedOnlineURL = HTMLonlineURL.replace("%data%", education.onlineCourses[course].url);
        $(".education-entry:last").append(formattedOnlineURL);
    }
};


//// function to display work experience
work.display = function() {
    work.jobs.forEach(function(job) {
        // create new div for work experience
        $("#workExperience").append(HTMLworkStart);
        // concat employer and title
        var formattedEmployer = HTMLworkEmployer.replace("%data%", job.employer);
        var formattedTitle = HTMLworkTitle.replace("%data%", job.title);
        var formattedEmployerTitle = formattedEmployer + formattedTitle;
        $(".work-entry:last").append(formattedEmployerTitle);

        var formattedDates = HTMLworkDates.replace("%data%", job.dates);
        $(".work-entry:last").append(formattedDates);

        var formattedLocation = HTMLworkLocation.replace("%data%", job.location);
        $(".work-entry:last").append(formattedLocation);

        var formattedDescription = HTMLworkDescription.replace("%data%", job.description);
        $(".work-entry:last").append(formattedDescription);
    });
};


//// function to display project experience

projects.display = function() {
    projects.projects.forEach(function(project) {
        $("#projects").append(HTMLprojectStart);
        var formattedsproject = HTMLprojectTitle.replace("%data%", project.title);
        $(".project-entry:last").append(formattedsproject);

        var formattedsplace = HTMLprojectDates.replace("%data%", project.description);
        $(".project-entry:last").append(formattedsplace);

        var formattedsdate = HTMLprojectDescription.replace("%data%", project.dates);
        $(".project-entry:last").append(formattedsdate);

        var formattedsimage = HTMLprojectImage.replace("%data%", project.images);
        $(".project-entry:last").append(formattedsimage);
    });
};


//// call all of the display functions
//calls display bio function
bio.display();
//calls display education function
education.display();
//calls display work function
work.display();
//calls display projects function
projects.display();


//// Adds Google Map
$("#mapDiv").append(googleMap);
