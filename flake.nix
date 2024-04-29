{
  description = "A very basic flake";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-unstable";
  };

  outputs = { self, nixpkgs }:
    let
        system = "x86_64-linux";
        pkgs = nixpkgs.legacyPackages.${system};
        # I hace realized that the comlexity of a flake largely depends on what system you are using. I am using linux
        # so I will be using x86_64-linux, everything else will be made as simple as possible.
        # ie. only one system and only one shell.

        # I will still be using the python.withPackages function to download python with the stated extra packages, because
        # it seems beter than isntalling them seperatly in the buildInputs.

        # picking a python version
        python = pkgs.python311;
    in {
        devShell.${system} = pkgs.mkShell{
            packages = [
                # downloading python with stated extra packages
                (python.withPackages (ps: with ps; [
                    pip
                    jupyter
                    pandas
                ]))
            ];
        };
    };
}


