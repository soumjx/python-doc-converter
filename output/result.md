This is a Heading

This is a paragraph

This structure:

• Is modular• Is extensible• Is testable• Is packaging-ready• Is enterprise-compliant

🧠 STRIVER 2 POINTERS & SLIDING WINDOWS — MASTER THEORY NOTES

Why This Topic Is Different

This is not a formula-memorization topic.

This is a constructive algorithmic framework:

You understand the behavior of the window, then mold the template based on the problem.

Most interview problems are variations of these patterns.

THE 4 MASTER PATTERNS

Every sliding window / two-pointer problem falls into one of these four.

PATTERN 1 — CONSTANT WINDOW

“Pick K consecutive elements and optimize something.”

Example:

Max sum of K consecutive elements.

Window Behavior

Window size is fixed

Slide window one step at a time

Algorithm

Compute initial sum for first window [0 → K-1]

Slide window:

Remove left element

Add next right element

Keep updating max/min

Template

L = 0, R = K-1

sum = sum(arr[L…R])

while (R < n) {

    maxSum = max(maxSum, sum)

    sum -= arr[L]; L++

    R++

    if (R < n) sum += arr[R]

}

Time: O(n)Space: O(1)

Rare in interviews but fundamental.

PATTERN 2 — LONGEST SUBARRAY / SUBSTRING (MOST IMPORTANT)

Find the longest window satisfying a condition.

Example:

Longest subarray with sum ≤ K.

Brute Force

Generate all subarrays.

for i = 0 → n-1:

    sum = 0

    for j = i → n-1:

        sum += arr[j]

        if sum ≤ K:

            maxLen = max(maxLen, j-i+1)

Time: O(n²)

Sliding Window (Better)

Maintain dynamic window.

Key Ideas

R → expands window

L → shrinks window

Expand while valid

Shrink when invalid

Standard Template

L = 0, R = 0, sum = 0, maxLen = 0

while (R < n) {

    sum += arr[R]

    while (sum > K) {      // shrink

        sum -= arr[L]

        L++

    }

    maxLen = max(maxLen, R-L+1)

    R++

}

Time: O(2n) → O(n)Space: O(1)

Optimization → TRUE O(n)

If only length is required (not subarray itself):

Replace while with if

if (sum > K) {

    sum -= arr[L]

    L++

}

This prevents unnecessary shrinking.

PATTERN 3 — NUMBER OF SUBARRAYS

Count subarrays satisfying condition (NOT length).

Example:

Number of subarrays with sum = K.

Trick Used

count(sum == K)

= count(sum ≤ K) – count(sum ≤ K-1)

So you reuse Pattern 2 twice and subtract.

PATTERN 4 — MINIMUM / SHORTEST WINDOW

Find smallest window satisfying a condition.

Behavior

Expand until condition becomes valid

Then aggressively shrink

Store smallest valid window

Mental Flow

Expand → valid → shrink → store answer → expand again

Used for:

Minimum window substring

Smallest subarray with sum ≥ K

FINAL MASTER TRUTHS

What changes

What never changes

Condition logic

Window expansion

Map/set usage

Shrinking logic

Constraint checking

Two pointers

Storage of result

Sliding behavior

Sliding Window Complexity Rule

Even though loops appear nested:

R moves at most n times

L moves at most n times→ Total operations = 2n = O(n)

You now possess the blueprint behind 90% of sliding window problems.

From here on, you’re no longer learning problems —you’re recognizing window behavior patterns.

When you want, send the next Striver problem and we convert it into weapons again.
