from particle_automata.particle import Particle


def test_particle():
    particle = Particle(1, 1)
    assert particle.x == 1
    assert particle.y == 1
    assert particle.type is None
    assert particle.color is None
    assert particle._has_changed_this_loop is False
    assert particle._acc_forces == []
    assert isinstance(particle.id, int)

def test_particle_movement():
    particle = Particle(1, 1)
    particle.move(x=2)
    assert particle.x == 2
    particle.move(y=2)
    assert particle.y == 2
