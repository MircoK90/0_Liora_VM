#!/bin/bash


BASE="http://localhost:8000"    # No! " = "

echo "HEALTH check"
curl -s "$BASE/healt" | python3 -m json.tool


echo ""
echo "===1. MQB - 5 Questions Alice"
# split wit "" -H "" for Authendification
curl -s -X GET \
    "$BASE/mcq?use=Positioning%20test&subjects=Databases&n=5" \
  -H "Authorization: Basic alice:wonderland" \
  | python3 -m json.tool


echo ""
echo "==2. MQB - 5 Questions Bob Buldier"
echo -s -X GET \
    "$BASE/mcq?use=Positioning%20test&subjects=Databases,Distributed%20systems&n=5" \
    -H "Authorization: Basic bob:builder" | python3 -m json.tool


echo ""
echo "==3. MQB - Wrong PW"
curl -s -X GET \
  "$BASE/mcq?use=Positioning%20test&subjects=Databases&n=5" \
  -H "Authorization: Basic alice:wrongpassword" \
  | python3 -m json.tool


echo ""
echo "== 4. missing auth header -H ..."
curl -s -X GET \
  "$BASE/mcq?use=Positioning%20test&subjects=Databases&n=5" \
  | python3 -m json.tool


echo ""
echo "== 5. invalid n (not 5/10/20)"
curl -s -X GET \
  "$BASE/mcq?use=Positioning%20test&subjects=Databases&n=3" \
  -H "Authorization: Basic alice:wonderland" \
  | python3 -m json.tool


echo ""
echo "== 6. Admin add a new question"
curl -s -X Post "$Base/questions"\
    -H "Authorization: Basic admin:4dm1N"\
    -H "Content-Type: application/json" \
    -d '{
        "question" : "admin new question!?",
        "subject" : "Distributed systems",
        "use": "Positioning test",
        "correct": "A",
        "answerA": "admin new answer A",
        "answerB": "admin new answer B",
        "answerC": "admin new answer C",
        "answerD": "",
        }'
echo "6. Admin add a new question runs trough"

echo ""
echo "==7. Wrong admin pw"
curl -s -X Post "$BASE/questions" \
  -H "Authorization: Basic alice:wonderland" \
  -H "Content-Type: application/json" \
  -d '{
    "question": "NoAdmin new question",
    "subject": "Databases",
    "use": "Positioning test",
    "correct": "B",
    "answerA": "NoAdmin new answerA",
    "answerB": "NoAdmin new answerB",
    "answerC": "NoAdmin new answerC",
    "answerD": ""
  }' | python3 -m json.tool