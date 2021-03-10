#!/usr/bin/perl

open(OUTPUT,"$ARGV[0]");
open(FILEOUT,"> $ARGV[1]");

while(<OUTPUT>){
        chomp;
        if($_ =~ /Key:\s*(.+?):\s*Value:\s*(.+?):\s*\/(.+?) =/){
                print FILEOUT "$1\t$3\n";
        }
}
close FILEOUT;

