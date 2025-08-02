{
  description = "Grokking FP development environment with Scala";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
      in
      {
        devShells.default = pkgs.mkShell {
          buildInputs = with pkgs; [
            # Python environment (existing)
            python313
            uv

            # Scala environment
            scala_3
            sbt
            jdk11

            # Optional: metals for IDE support
            metals
          ];

          shellHook = ''
            echo "🎯 Grokking FP Development Environment"
            echo "Python: $(python --version)"
            echo "Scala: $(scala -version 2>&1)"
            echo "SBT: $(sbt --version)"
            echo ""
            echo "Python exercises: python src/main/ch01_intro.py"
            echo "Scala REPL: scala"
            echo "Create Scala project: sbt new scala/scala3.g8"
          '';
        };
      });
}
