if command -v python
then
    if $(python -V 2>&1 | grep -Po '(?<=Python )(.)') == '3'
    then
        python ./square.py
    else
        echo "Python 3 is required"
    fi
elif command -v python3
then
    if $(python3 -V 2>&1 | grep -Po '(?<=Python )(.)') == '3'
    then
        python3 ./square.py
    else
        echo "Python 3 is required"
    fi
elif command -v py
then
    if $(py -V 2>&1 | grep -Po '(?<=Python )(.)') == '3'
    then
        py ./square.py
    else
        echo "Python 3 is required"
    fi
elif command -v py3
then
    if $(py3 -V 2>&1 | grep -Po '(?<=Python )(.)') == '3'
    then
        py3 ./square.py
    else
        echo "Python 3 is required"
    fi
else
    echo "Could not find python, python3, py or py3, if you are using another alias run square.py with python 3"
fi