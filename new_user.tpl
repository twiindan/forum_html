<h2>Create new User</h2>
<form action="/v1.0/users" method="POST">
NAME: <input type="text" size="100" maxlength="100" name="name" id="name"><br>
USERNAME: <input type="text" size="100" maxlength="30" name="username" id="username"><br>
PASSWORD: <input type="password" size="100" maxlength="30" name="password" id="password"><br>
EMAIL: <input type="text" size="100" maxlength="100" name="email" id="email"><br>
<p>ROLE:<select name="role" id="role">
<option value="QA">QA</option>
<option value="DEVELOPER">DEVELOPER</option>
<option value="MANAGER">MANAGER</option>
</select>
</p>
<input type="submit" name="save" value="save" id="save">
</form>



