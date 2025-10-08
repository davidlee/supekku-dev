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

**A**: Not really, I mean you know enough from the specs - yeah, whatever, with
some caveats. The point is, it works fine as long as you work the way the
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
requirements still hold? Don't you risk having them ... build the new feature
without accounting for previous work?

**A**: Well, you have the test suite. And if you're diligent with your
research, you can pull most of the important context into the implementation
plan.

**Q**: Ok. Sounds like it can work ... but that it's fundamentally a massive
hack?

**A**: Sure, I kinda get where you're coming from, but this has been an
unsolved problem in software ... basically forever. And probably everything
that's tried to solve it so far has been worse, except probably Literate
Programming, which is probably amazing if your coworkers are Donald Knuth
instead of a stochastic mythomaniac chatbot.

**Q**: Right. But what if you invert the model?

**A**: But we already have, see? Spec-driven development is about making the
specs the main thing -

**Q**: Until you archive them and use the code as the system of truth? Hey
look, I got an idea. Mind if we swap for a sec?

**A**: Uh. Sure.

---

**A**: Ok. So why don't we start by _keeping_ the spec. Make it ... evergreen.

**Q**: We already do?

**A**: No, not piled up in the evidence locker, so you can dig through their detritus.

**Q**: How then?

**A**: First, you treat it as the actual system of truth - not something
disposable after it's done.

**Q**: Well that sounds nice. But how's it work? Say we've written our first
spec, for a static landing page. We've built a plan, gotten it done and tests
pass. Now we've gotta add login and a member area. What now?

**A**: Right. You change it. Have the changes to the spec drive the plan -
collect the delta, wrap it in enough context to turn it into an imperative
patch. Then break down the work and add verification steps like you're used
to.

**Q**: Spec's gonna drift though. How can it be the system of truth when it
doesn't reflect all the detours and adaptations and agent fuckups along the
way?

**A**: You said agents were pretty efficient at researching the codebase. So,
we add process hooks along the way to document and upstream anything important:
decisions, adaptations, issues. When you wrap each phase of your plan.
Incrementally feed them back into the spec if they're relevant, but continue
and adapt the plan, as long as it still holds overall.

Then when the plan's done, you run an audit. Verify the spec against the code,
make sure it's accurate and thorough enough you could regenerate the code
if you needed to.

**Q**: So this spec just gets bigger and bigger with each change?

**A**: Do I look like a moron? Of course not. Split it up, relationally. Use
markdown frontmatter and ids. We could use the C4 model terms for specs at
different levels of abstraction - most code probably has more than one
applicable spec, and that's fine.

**Q**: How so?

**A**: Track what has & hasn't made a roundtrip to mainline for each spec,
using git SHA refs.

When you want to implement some set of changes, you create a Delta (a markdown
artefact) to represent it: collect all the specs that apply, explicitly
reference the changed elements, and elaborate the design changes to ensure
they're coherent and act as a guide to details in the linked specs. It'll act
as the implementation guide for agents, and you review it carefully just like
you would your feature spec.

Then you build an Implementation Plan the same way you're used to.

**Q**: Isn't that kind of complicated? You have to stitch together context from
a bunch of different interlinked specs ...

**A**: No, I'm way too lazy. An agent can do that just fine.

I just kick off a command, make sure the inputs are correct and the changes
belong together, and then argue about the technical design until it's reasonable.

**Q**: What if you need to change the specs to make the design work?

**A**: Yes.

**Q**: Ok. And the benefit of all this is ... ?

**A**: Well, doing what you claimed earlier: primacy of the Spec. It's up to
date; you can use it to derive the code. You can actually trust it, understand
the entire system with it. You can change it, and have your modifications flow
into implementation, and integrate adaptations made along the way. And you can
make changes at any scale you want.

**Q**: Uh huh. And you've done this already?

**A**: Dude, are you drunk? You literally just explained what Spec-Driven Development
is to me. We've been standing here the whole time. I'm just explaining a better
idea.

---

''')),P(Img(alt="diagram", src="/assets/img/supekko-in-a-picture.png")))


serve()
