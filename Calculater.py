{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPDWGxZCWDVh1lv+9eS+rq3",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/yeminenicharanvenkat-nridegree/Python-mini-project/blob/main/Calculater.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 141
        },
        "id": "6ewzBElSyGi7",
        "outputId": "e3b38584-766c-4947-9f50-fa3f3b5dd55a"
      },
      "outputs": [
        {
          "output_type": "error",
          "ename": "IndentationError",
          "evalue": "unindent does not match any outer indentation level (<tokenize>, line 8)",
          "traceback": [
            "\u001b[0;36m  File \u001b[0;32m\"<tokenize>\"\u001b[0;36m, line \u001b[0;32m8\u001b[0m\n\u001b[0;31m    operator=int(input(\"Enter Arthmetical Operator [+,-,*,/,%]\\n\"))\u001b[0m\n\u001b[0m    ^\u001b[0m\n\u001b[0;31mIndentationError\u001b[0m\u001b[0;31m:\u001b[0m unindent does not match any outer indentation level\n"
          ]
        }
      ],
      "source": [
        "def cal():\n",
        "\n",
        "#Enter First Number\n",
        "    a=int(input(\"Enter Number\"))\n",
        "\n",
        "#Enter an Operator\n",
        "\n",
        "  operator=int(input(\"Enter Arthmetical Operator [+,-,*,/,%]\\n\"))\n",
        "  if operator != \"+\" && operator !=\"-\" && operator !=\"*\" && operator !=\"/\" && operator !=\"%\":\n",
        "     print(\"Arthmetical Operator Invalid\")\n",
        "     operator.exit(0)\n",
        "\n",
        "#Enter Second Number\n",
        "\n",
        "   b=int(input(\"Enter Number\"))\n",
        "\n",
        "   if a=int && b=int :\n",
        "      print(\" \")\n",
        "   else:\n",
        "      print(\"Enter valid Number\")\n",
        "\n",
        "#Procedure of calculation\n",
        "\n",
        "   elif operator == \"+\" :\n",
        "     res=a+b\n",
        "     print(\"Addition : \",res)\n",
        "\n",
        "  elif operator == \"-\" :\n",
        "     res=a-b\n",
        "     print(\"Subtraction : \",res)\n",
        "\n",
        "  elif operator == \"*\" :\n",
        "     res=a*b\n",
        "     print(\"Multiplication : \",res)\n",
        "\n",
        "  elif operator == \"/\" :\n",
        "     res=a/b\n",
        "     print(\"Division: \",res)\n",
        "\n",
        "  elif operator == \"%\" :\n",
        "     res=a%b\n",
        "     print(\"Modulo : \",res)"
      ]
    }
  ]
}