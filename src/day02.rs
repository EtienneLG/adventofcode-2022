use std::fs;

fn part_one() {
    let input = fs::read_to_string("inputs/day02.txt").expect("Nope");
    let rounds: Vec<Vec<&str>> = input.split("\r\n").map(|r| r.split(' ').collect()).collect();

    let pos = [("C", "Z"), ("B", "Y"), ("A", "X")];

    let mut points = 0;
    for r in rounds.iter() {
        let p = pos.iter().position(|x| x.1 == r[1]).unwrap();
        if r[0] == pos[(p + 1) % 3].0 {
            points += 6
        }
        else if r[0] == pos[p].0 {
            points += 3
        }
        points += 3 - p
    }

    println!("Part one ==> {:?}", points);
}

fn part_two() { 
    let input = fs::read_to_string("inputs/day02.txt").expect("Nope");
    let rounds: Vec<Vec<&str>> = input.split("\r\n").map(|r| r.split(' ').collect()).collect();

    let pos = [("C", "Z"), ("B", "Y"), ("A", "X")];

    let mut points: i32 = 0;
    for r in rounds.iter() {
        let p = pos.iter().position(|x| x.0 == r[0]).unwrap() as i32;    
        match r[1] {
            "Z" => points += 6 + 3 - (p - 1).rem_euclid(3),
            "Y" => points += 3 + 3 - p,
            _ => points += 3 - (p + 1).rem_euclid(3)
        }
    }

    println!("Part one ==> {:?}", points);
}

pub fn solve() {
    part_one();
    part_two();
}
