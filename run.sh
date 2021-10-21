if command -v python then
    if $(python -V 2>&1 | grep -Po '(?<=Python )(.)') == '3' then
        python .square.py
        exit()
    fi
fi

if command -v python3 then
    if $(python3 -V 2>&1 | grep -Po '(?<=Python )(.)') == '3' then
        python3 ./square.py
        exit()
    fi
fi

if command -v py then
    if $(py -V 2>&1 | grep -Po '(?<=Python )(.)') == '3' then
        py ./square.py
        exit()
    fi
fi

if command -v py3 then
    if $(py3 -V 2>&1 | grep -Po '(?<=Python )(.)') == '3' then
        py3 ./square.py
        exit()
    fi
fi

echo "python, python3, py, py3 not found with a python 3 version"