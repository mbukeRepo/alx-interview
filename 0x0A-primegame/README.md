<div class="panel-body">
    <span id="user_id" data-id="1066"></span>
<p>Maria and Ben are playing a game. Given a set of consecutive integers starting from <code>1</code> up to and including <code>n</code>, they take turns choosing a prime number from the set and removing that number and its multiples from the set. The player that cannot make a move loses the game.</p>

<p>They play <code>x</code> rounds of the game, where <code>n</code> may be different for each round. Assuming Maria always goes first and both players play optimally, determine who the winner of each game is.</p>

<ul>
<li>Prototype: <code>def isWinner(x, nums)</code></li>
<li>where <code>x</code> is the number of rounds and <code>nums</code> is an array of <code>n</code> </li>
<li>Return: name of the player that won the most rounds</li>
<li>If the winner cannot be determined, return <code>None</code></li>
<li>You can assume <code>n</code> and <code>x</code> will not be larger than 10000</li>
<li>You cannot import any packages in this task</li>
</ul>

<p>Example:</p>

<ul>
<li><code>x</code> = <code>3</code>, <code>nums</code> = <code>[4, 5, 1]</code></li>
</ul>

<p>First round: <code>4</code></p>

<ul>
<li>Maria picks 2 and removes 2, 4, leaving 1, 3</li>
<li>Ben picks 3 and removes 3, leaving 1</li>
<li>Ben wins because there are no prime numbers left for Maria to choose</li>
</ul>

<p>Second round: <code>5</code></p>

<ul>
<li>Maria picks 2 and removes 2, 4, leaving 1, 3, 5</li>
<li>Ben picks 3 and removes 3, leaving 1, 5</li>
<li>Maria picks 5 and removes 5, leaving 1</li>
<li>Maria wins because there are no prime numbers left for Ben to choose</li>
</ul>

<p>Third round: <code>1</code></p>

<ul>
<li>Ben wins because there are no prime numbers for Maria to choose</li>
</ul>

<p><strong>Result: Ben has the most wins</strong></p>

<pre><code>carrie@ubuntu:~/0x0A-primegame$ cat main_0.py
#!/usr/bin/python3

isWinner = __import__('0-prime_game').isWinner


print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))

carrie@ubuntu:~/0x0A-primegame$
</code></pre>

<pre><code>carrie@ubuntu:~/0x0A-primegame$ ./main_0.py
Winner: Ben
carrie@ubuntu:~/0x0A-primegame$
</code></pre>
</div>
