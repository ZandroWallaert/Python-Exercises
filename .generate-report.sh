# remove previous report file and other garbage
git clean -xf
git pull --all 	
git br --all --format="%(refname)" | grep -oP "remote.*\K(student-.*)" | while read -r branch; do
    echo "branch $branch " >> raw
    git checkout $branch
    nosetests3 -v >> raw 2>&1 # TODO nosetests for mac
done
# filter out test failure tracebacks
cat raw | grep -P "^test0|branch.*" >> report
rm raw
