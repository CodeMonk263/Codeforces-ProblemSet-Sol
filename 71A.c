#include <cstdio>
#include <cstring>

using namespace std;

int main(int argc, const char * argv[])
{
    int testCases;

    scanf ("%d", &testCases);

    char word [100 + 10];

    while ( testCases-- ) {

        scanf ("%s", word);

        int length = (int) strlen (word);

        if (length > 10) {
            printf ("%c%d%c\n", word [0], length - 2, word [length - 1]);
        } else {
            printf ("%s\n", word);
        }

    }

    return 0;
}
