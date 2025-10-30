# LocalLink 🛠️ — Community Service Directory

*A hyperlocal, map-enabled classified app for communities and campuses.*

---

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Design Decisions](#design-decisions)
- [Screenshots & Flow](#screenshots--flow)
- [Team Contributions](#team-contributions)
- [Key Concepts Used](#key-concepts-used)
- [Setup & Installation](#setup--installation)
- [Challenges Faced](#challenges-faced)
- [Future Improvements](#future-improvements)
- [Requirements.txt](#requirementstxt)
- [License](#license)

---

## Introduction

**LocalLink** is a Django-based platform for connecting local service providers and seekers in any Indian neighborhood, college, or city. Users can list, search, sort, and review services like tutors, electricians, or pet sitters on an interactive map.

---

## Features

- **Service Listings:** CRUD for location-based services (with map pin).
- **Categories:** All services are organized.
- **Reviews:** 5-star rating and comment system; shows review count and average everywhere.
- **Browse & Search:** Filter services by text, category, location, or geography.
- **Sort by Nearest:** Uses your location (or an address) to sort results by physical proximity.
- **Map Integration:** Interactive OpenStreetMap (Leaflet.js) for both address entry and viewing.
- **Indianized Demo Data:** Real Indian cities, names, phone numbers, and reviews in all sample content.
- **Session-based Ownership:** Only the service creator can edit or delete their listing (secure, simple UX).
- **Responsive Design:** Modern UI (TailwindCSS), optimized for desktop, tablet, mobile.

---


## Project Structure

```
LocalLink/
├── locallink/           # Django project settings
├── services/            # Main application
│   ├── models.py       # Database models
│   ├── views.py        # View functions
│   ├── forms.py        # Django forms
│   ├── admin.py        # Admin configuration
│   ├── urls.py         # URL patterns
│   └── management/     # Custom management commands
├── templates/          # HTML templates
│   ├── base.html       # Base template
│   └── services/       # Service-specific templates
├── manage.py           # Django management script
└── requirements.txt    # Python dependencies
```


### Database Models

#### **Category**
- `id` (auto)
- `name` (str, unique)
- `description` (str)
- `created_at` (datetime)

#### **ServiceListing**
- `id` (auto)
- `service_name` (str)
- `provider_name` (str)
- `contact_info` (str)
- `email` (str)
- `phone` (str)
- `description` (str)
- `location_area` (str)
- `latitude` (`float`)  ← used for map/sorting
- `longitude` (`float`) ← used for map/sorting
- `category` (FK → Category)
- `price_range` (str)
- `is_available` (bool)
- `created_at`, `updated_at` (datetime)

#### **Review**
- `id` (auto)
- `service_listing` (FK → ServiceListing)
- `reviewer_name` (str)
- `rating` (int, 1–5, drop-down)
- `comment` (text)
- `created_at` (datetime)

---

## Design Decisions

- **Mapping:** Used Leaflet.js and OpenStreetMap for free, reliable map UI—no API keys/billing required.
- **Ownership:** Listings are editable only in the creator’s browser/session (simple for MVP, avoids registration hassle).
- **Search UX:** Auto-fills form fields with GET parameters; keeps search bar and filters consistent for great UX.
- **Data Indianization:** Sample data references Indian names, cities, and phone numbers for local relevance.
- **Fallback content:** “Browse Services” page always displays featured listings or a strong CTA even when filters are too strict or DB is empty.
- **Sorting Nearest:** Haversine formula used (in Python) to compute proper geo distance between user and all listings.

---

## Screenshots & Flow

- Homepage with categories & featured_


![Home Page](screenshots\1_homepage.png)
![Home Page](screenshots\1_homepage(2).png)
![Home Page](screenshots\1_homepage(3).png)
![Home Page](screenshots\1_homepage(4).png)



- Service browse/search page (results, filtering, fallback)_ Service details page (with map, reviews, provider info)_

```
![Browse Services](screenshots\2_browse.png)
![Browse Services](screenshots\2_browse(2).png)
![Browse Services](screenshots\2_browse(3).png)
![Browse Services](screenshots\5_reviews.png)

```
- Add/Edit form with map location picker_
```
![Map Pick](screenshots\4_map_pick.png)

```

- Service Listings with details
```
![Service Listings](screenshots\listingservice.png)
![Service Listings](screenshots\listingservicedetails.png)
```


---

## Team Contributions

| Team Member              | Contribution Areas                                              |
|--------------------------|-----------------------------------------------------------------|
| [Sanika Jage 333]        | Django Models & Admin, Database schema, CRUD forms              |
| [Vanshita Sonkar 338]    | Map Integration, Service list/search UI, Geo-sorting/logics     |
| [Pranjal Jadhav 345]     | Reviews & Ratings System, Demo Data Population, Indianization   |
| [Himani Shrivastava 324] | UX & Styling (Tailwind), Template fallback logic, bug fixing    |
|--------------------------|-----------------------------------------------------------------|

---

## Key Concepts Used

- **Django ORM:** All DB models and queries use class-based models and QuerySet filtering.
- **Views, Routing & Templates:** Each CRUD, search, map, and review operation flows through Django’s powerful view/template pipeline.
- **Forms & Widgets:** Django forms auto-generate UI, and custom widgets (e.g., hidden fields for lat/lng) enable map integration.
- **Leaflet JS:** Pure-JS, open-source mapping used for geolocation, with event-listeners to update form fields on user input.
- **List comprehensions & model methods:** To annotate or filter listings in complex ways (e.g., review averages).
- **Session management:** For simple, secure ownership of listings.
- **Separation of concerns:** Models handle business rules, views control logic, templates present UI.

#### Example Course Concepts Directly Applied:
- Used list comprehensions to process collections, e.g., `[review.rating for review in reviews]`
- Used Django’s pagination and QuerySet chaining to chain filters and sorts.
- Haversine distance computation (applied in Python) to optimize nearby service search.
- Iterative/conditional rendering in templates (e.g., showing fallback listings).

---

## Setup & Installation

### 1. Clone & Install
```bash
git clone <repo-url>
cd LocalLink
pip install -r requirements.txt
```

### 2. Database Setup
```bash
python manage.py migrate
```

### 3. (Optional) Demo Data
```bash
python manage.py populate_data
```

### 4. Run Server
```bash
python manage.py runserver
```

Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/)  
Admin: `/admin/` (make superuser for full admin access)

---

## Challenges Faced

- **Map JS/HTML integration:** Ensuring dynamic map display works on all browsers and forms.
- **Persistent Search/Filter Bar:** Keeping user input fields “sticky,” so experience is never confusing (with many filter options applied).
- **Fallback UX for Empty Results/DB:** Ensured that even with no matches/database entries, page remains welcoming.
- **Indianization of Data:** Had to build custom sample data logic for names, cities, and phone numbers.
- **Session Ownership:** Balancing privacy with usability in a system without registrations.

---

## Future Improvements

- Add mobile location auto-detection on every “List a Service”.
- OAuth/phone-based signup (beyond session-based ownership).
- Profile pages for providers/seekers.
- Photo gallery for each listing.
- Direct messages or WhatsApp links.
- “Top rated” or promoted listings with premium features.
- Email/notification system for new reviews or booking requests.
- More robust map search (multi-city, polygon area support).

---

## requirements.txt

```
Django>=5.2.0
```
_Also required for maps (Leaflet.js) but loaded via CDN in templates._

---
## Conclusion

LocalLink taught us how to connect backend logic with an interactive, map-based frontend while focusing on clean architecture, usability, and local context relevance. Through this project, we deepened our understanding of Django models, forms, and templates, and learned to integrate real-world geolocation features into web applications.



---

**[Reserve these sections for annotated screenshots - fill in after you run the application and grab relevant UI shots.]**


