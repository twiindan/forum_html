
%if first_time:
    <h1 id="header_first_time">Welcome to ExpoQA Python Forum</h1>


%else:
    <h1 id="header_other_times">Welcome back! Nice to see you again in ExpoQA Forum</h1>

%end

<a id="create_user" href="http://localhost:8081/v1.0/users/new">Create a new user</a><br>
<a id="list_users" href="http://localhost:8081/v1.0/users">List users</a><br>
<a id="create_message" href="http://localhost:8081/v1.0/forum/new">Create new forum message</a><br>
<a id="list_messages" href="http://localhost:8081/v1.0/forum/">List forum message</a><br>
