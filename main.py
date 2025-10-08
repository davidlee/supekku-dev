from fasthtml.common import *
import mistune

app,rt = fast_app()

@rt('/')
def get():
    return Titled("Supekku.dev", Div(P("if you came here looking for ritual self-disembowellment, you have a typo"),P(A("ok. What's a spec?",href="/spec-driven-development"))))

@rt('/spec-driven-development')
def get():
    return Titled("Supekku.dev", NotStr(mistune.html(
'''
## Spec-driven development

**Q**: So what's this spec-driven thing you keep talking about?

**A**: Oh, Spec-driven development is super nice. The ideas is to write a
detailed spec for each big set of changes, usually organised around delivering
a "feature".

**Q**: Right. So you have a nice spec, you build an implementation plan around
it, break it down, and you (or your agent) can refer to the spec for details
while your're implementing?

**A**: Exactly. Getting all the requirements in place, designing a solution,
deciding how to verify it works, reviewing it and kicking the tyres a bit
before you build ... it's a good idea anyway, but when agents are doing the
build, it's pretty much the only approach that works.

**Q**: I can imagine. And then when you're done with the feature, you've got a
nice specification that describes exactly how your application works. So once
you've shipped and you're on to the next feature, how does changing the
original spec work?

**A**: Oh, each feature gets it's own spec. So, you write a new one.

**Q**: Ahh. So it's just a point in time thing?

**A**: Yeah, that's right.

**Q**: So, if I want to understand the codebase after I've shipped a few
features?

**A**: Well, you could find all the specs that applied changes to the code
you're interested in. Then, look at them in order, to build up a picture of the
current state of the system. Or just read the code.

**Q**: Seriously?

**A**: Obviously nobody wants to do that. So you get a research agent to go
inspect the code, and cross-reference historical specs for understanding.
That's one of the main inputs into writing a new spec.

**Q**: And that's actually practical? It sounds incredibly inefficient.

**A**: Actually, With the right prompt and template, agents are surprisingly
good at it. So yeah, I get why it sounds sketchy, but it really works pretty
well.

**Q**: So you just reverse-engineer the architecture of the whole codebase
every time you want to make a plan?

**A**: Well, no, not the whole thing. Just just the parts you need to work in.

**Q**: Right. So ... you're kinda flying blind when it comes to everything else?

**A**: Well, if you just build everything as disposable microservices -

**Q**: Look, I get the appeal, I really do. But no.

**A**: Alright, fine. The point is, it works fine as long as you work the way the
system kind of wants you to work.

**Q**: So how's that ... kinda like waterfall?

**A**: What? No! I mean, you do end up kinda nudged towards long-lived
branches, delivering an entire feature at a time, and integrating a bunch of
agent sessions worth of work all at the end.

**Q**: Right. Long-lived feature branches, big merges, deferred integration ...
agents might be new, but doesn't all this feel a bit ... regressive? Not to
mention inelegant?

**A**: I dunno man, have you ever tried to work with an agent without a
watertight plan? I think it's just the only way of working with them that makes
sense.

**Q**: So how do you make sure when you're building out a new feature, that all
the specs from the previous ones are taken into consideration and their
requirements still hold? Don't you risk them bulldozing through the old
stuff whenever they build something new?

**A**: Well, you have the tests. And if you're diligent with your research, you
can pull most of the important context into the implementation plan. Or, you
know. Microservices.

**Q**: Right. I mean, I'm sure it can work, but is that really the best we can
do?

**A**: I kinda get where you're coming from, but the exact thing you're taking
issue with has been an unsolved problem in software ... basically forever. And
probably everything that's tried to solve it so far has been worse, except
Literate Programming, which I'm sure is amazing if your coworkers are Donald
Knuth instead of a stochastic mythomaniac chatbot.

**Q**: But ... ok. What if you ... invert the model?

**A**: But that's exactly what it does! Spec-driven development is about making
the code serve the specifications -

**Q**: Sure, until you finish implementing them - then you're back to software
archaeology. Nah. Look, I got an idea. Mind if we swap for a sec?

**A**: Uhh. Sure.

---

**A**: Ok. So we start by _keeping_ the specs. Make them evergreen.

**Q**: We ... already do?

**A**: No, not piled up in the evidence locker, so you can dig through their detritus.

**Q**: How, then?

**A**: You treat them as the actual system of truth - not something disposable
after they've hit the main branch. They have to be able to change.

**Q**: Well, that sounds nice. But how's it supposed to work? Say we've written
our first spec, for a static landing page. We've built a plan, gotten it done
and tests pass. Now we've gotta add login and a member area. What now?

**A**: Have your _changes_ to the spec produce the implementation plan - collect
the delta, assemble enough surrounding context to produce a design doc, and
massage it into shape. Then break down the work and add verification steps like
you're used to.

**Q**: Spec's gonna drift out of alignment with the code, though. How can it be
the system of truth when it doesn't reflect all the detours and adaptations and
agent fuckups along the way?

**A**: You said agents were pretty efficient at researching the codebase. So,
we add process hooks along the way to document and upstream anything important:
decisions, adaptations, issues, when you wrap up each phase of the plan. Feed
them back into the spec if they're relevant, but continue and adapt, as long as
it still holds overall.

Then when your'e done implementing, you run a lightweight audit. Verify the
spec against the changed code, make sure it's accurate and thorough enough you could
recreate it if you needed to.

It's no more than you're already doing as "research", but this way you can keep
your view of the entire codebase current.

**Q**: So ... this one spec just gets bigger and bigger with each change?

**A**: Do I look like a moron? Of course not. Split it up however you like.
Keep product your requirements, high level views of subsystems, and drill down
into details for every file or module. Markdown frontmatter and ids to link them
are all you need.

Most of the time a given file's going to have more than one spec that applies,
at different levels of abstraction - and that's fine, as long as you have a few
conventions (give your requirements IDs, for instance). Just have an agent
bundle what's applicable to the changes.

**Q**: So what, everything in every spec that applies, for every bit of code
you're touching?

**A**: No ... no. track what's made a roundtrip to mainline within each spec.
Mark up the SHA refs, or just use checkboxes. Or just collect the SHAs with
the spec changes you want to ship, if you're ok with a slightly blunt
instrument. The actual mechanics aren't hard, if you can write a prompt.

When you want to implement some set of changes, you create a Delta (just a
markdown doc) to represent it: collect all the specs that apply, list the
requirements with their IDs, link everything up in the frontmatter, and
elaborate the design changes to ensure they're coherent. This is the
implementation guide for agents, and you review it carefully, just like you
would your feature spec.

Then you build an Implementation Plan the same way you're used to.

**Q**: Isn't that all a bit complicated? You have to stitch together context from
a bunch of different interlinked specs ...

**A**: Man, I'm not doing it, I'm way too lazy. An agent can manage it just fine,
though.

It's just: kick off a canned prompt, make sure the inputs are correct and the
changes make sense together, and then argue with robot about the technical
design as usual, until it's a reasonable plan.

**Q**: What if you need to change the specs to make the design work?

**A**: Of course. Revise them, and update the Delta.

**Q**: Ok. And the benefit of all this is ... ?

**A**: Well, actually doing what you claimed earlier: primacy of the Spec. It's
up to date; you can use it to derive the code. You can actually trust it,
understand the entire system with it. You can change it, and have your
modifications flow into implementation, and integrate adaptations made along
the way. And you can make changes at any scale you want. You could even build
something bigger than you can afford to just throw away and boil the South
Pacific to regenerate.

**Q**: Uh huh. And I suppose you've done this already?

**A**: Are you drunk? You literally just explained what Spec-Driven Development
is to me. We've been talking here for exactly as long as I've known about it.
I'm just explaining how to improve it.

---

''')),
    P(Img(alt="diagram", src="/assets/img/supekko-in-a-picture.png")),
    P(A("spec-kit",href="https://github.com/github/spec-kit/blob/main/spec-driven.md")))


serve()
