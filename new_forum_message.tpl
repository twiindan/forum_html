<p>Publish in a forum</p>
<form action="/v1.0/forum" method="POST">
<p>THEME:<select name="theme">
<option value="Security">Security</option>
<option value="Development">Development</option>
<option value="Automation">Automation</option>
<option value="Testing">Testing</option>
</select>
</p>
SUBJECT: <input type="text" size="100" maxlength="100" name="subject"><br>
MESSAGE: <input type="text" size="100" maxlength="100" name="message"><br>
<input type="submit" name="save" value="save">
</form>


