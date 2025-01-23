{% if first_time %}
    <h1 id="header_first_time">Welcome to Testing Python Forum</h1>
{% else %}
    <h1 id="header_other_times">Welcome back! Nice to see you again Testing Forum</h1>
{% endif %}

<a id="create_user" href="https://forum-testing.herokuapp.com/v1.0/users/new">Create a new user</a><br>
<a id="list_users" href="https://forum-testing.herokuapp.com/v1.0/users">List users</a><br>
<a id="create_message" href="https://forum-testing.herokuapp.com/v1.0/forum/new">Create new forum message</a><br>
<a id="list_messages" href="https://forum-testing.herokuapp.com/v1.0/forum/">List forum message</a><br>
