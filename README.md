# PROJECT OVERVIEW

The KPM Beranang Vehicle Management Online System is a web-based platform designed
to facilitate the rental and booking of vehicles provided by the college. The system aims to
streamline the process of accessing college vehicles for various purposes, adding a new
vehicle, keep tab on maintenance, and of course the bookings.

**Target User and Accessibility:**

KPMB Staff and Faculty: Staff and faculty members who need to book vehicles for official
college-related purposes, such as attending conferences, conducting field trips, or
transporting equipment. They can book various available vehicle such as cars, van,
motorcycles and busses.

KPMB Students: Registered students that require transportation for events, excursions, or
community outreach programs. Student’s can only book cars and motorcycles.

KPMB Administrator: Administrative staff responsible for managing vehicle reservations,
maintaining vehicle records, and overseeing the overall operation of the system.

**Project Purpose:**

Vehicle Booking and Rental: Users can easily book and rent college vehicles online for
official purposes like conferences, field trips, or events.

Efficient Resource Management: Administrators can efficiently manage vehicle resources,
track usage, and optimize scheduling to avoid conflicts.

User Accountability and Tracking: The system tracks user activities and booking history,
ensuring transparency and accountability for vehicle usage.

Providing Transport to KPM students: Ease of transportation becomes an essential to all as
some courses like the diploma students of Landscape and Horticultur needs a lot of mobility
to go on site visits off class.

Streamlined Administrative Tasks: The administrative page simplifies tasks like managing
bookings, handling maintenance, and vehicles inventory.


**Type of Users:**

Superusers: Deals with any critical conflict in database, collecting raw data and granting
administrator status to selected users.

Administrator: Task on adding and updating the vehicle and keep tab on maintenance ad
have a special assigned pages for this user only.

Student and Lecturer Status: Able to book the actual vehicle one at a time only. Students are
restricted to book only cars and motorcycles.

# WEBSITE FLOW:

**Administrator View:**

Administrators must be created thru the Django-admin page granted by the superuser. After
registering with the superuser administrators can now proceed to login.


After administrator logged in, it will be greeted by the homepage with dashboard on vehicle
count which is also visible to student and lecturer status.


Firstly, we’ll show the administration process of the website. The administrator click on
Vehicle on the navigation bar to add a new vehicle after entering the appropriate information
the user adds the vehicle and a message should appear saying “New vehicle has been
added”. Click on Back to Homepage to return.



Vehicle will only have four types (van, motorcycle, car, bus) and the Status of the vehicle will
be available, reserved and under maintenance next one is about Maintenance. It is pretty
much the same with Vehicle.


Concludes the administration role on the website. Clicking Log Out will throw you back to the

Welcome page.


**Student and Lecturer Status View:**

Going thru the student or staffer’s view, users have to register themselves by entering the
credentials appropriately in order to differentiate students from staffer’s.


Once again, we are greeted with the same homepage but with limited navbar.


After making a booking anew navbar clickable link appear that will redirect the user to his
bookings.

User can change the reservation date but unable to switch vehicle. Once clicked Update
Booking refresh the site. The new updated data shall be present.


**Additional:**

Once logged out in the homepage the user should be redirected to the Welcome page and
the user may login back in.
