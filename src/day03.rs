use std::fs;
use std::collections::HashSet;

pub fn solve() {
    let rucksacks = fs::read_to_string("inputs/day03.txt").expect("Problem");
    
    let letters: Vec<char> = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ".chars().collect();
    
    let compartments = rucksacks.split("\r\n")
    .map(|c| (c[..c.len()/2].chars().collect::<HashSet<char>>(), c[c.len()/2..].chars().collect::<HashSet<char>>()))
    .fold(0, |a, b| a + letters.iter()
        .position(|x| x==b.0.intersection(&b.1).last().unwrap()).unwrap() + 1
    );

    let badges = rucksacks.split("\r\n")
    .map(|c| c.chars().collect::<HashSet<char>>())
    .fold((0, HashSet::from_iter(letters.iter().cloned())), |a, b|
        if a.1.intersection(&b).count() == 1
        { (a.0 + 1 + letters.iter().position(|x| x==a.1.intersection(&b).last().unwrap()).unwrap(), 
            HashSet::from_iter(letters.iter().cloned())) } 
        else { (a.0, 
            HashSet::from_iter(a.1.intersection(&b).cloned())) }
    ).0;

    println!("Part one ==> {} \r\nPart two ==> {}", compartments, badges);
}