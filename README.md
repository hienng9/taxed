<div align="center">

# Taxed Website
</div>

### Cloning the repository

--> Clone the repository using the command below :
```bash
git clone https://github.com/hienng9/taxed.git

```

--> Move into the directory where we have the project files : 
```bash
cd taxed

```

--> Create a virtual environment :
```bash
# Let's install virtualenv first
pip install virtualenv

# Then we create our virtual environment
virtualenv envname

```

--> Activate the virtual environment :
```bash
envname\scripts\activate

```

--> Install the requirements :
```bash
pip install -r requirements.txt

```

#

### Running the App

--> To run the App, in one terminal:

```bash
python3 -m celery -A taxedwebsite worker -l info

```
open another terminal, run the following:

```bash
python3 manage.py runserver

```

> ⚠ Then, the development server will be started at http://127.0.0.1:8000/

<tr>
<td width="50%">      
&nbsp; 
<br>
<p align="center">
  Feed Home
</p>
<img src="https://user-images.githubusercontent.com/72341453/134747262-0a92233d-8010-40f8-84c5-8d94895aac44.PNG">
</td> 
<td width="50%">
<br>
<p align="center">
  Room Conversation Preview
</p>
<img src="https://user-images.githubusercontent.com/72341453/134747155-3ca5b55f-b064-4741-aeae-abe90bddf41e.PNG">  
</td>
</table>


