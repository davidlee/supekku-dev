{
  description = "A simple development shell";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable"; # Specify a stable Nixpkgs channel
  };

  outputs = {
    self,
    nixpkgs,
  }: {
    devShells.x86_64-linux.default = nixpkgs.legacyPackages.x86_64-linux.mkShell {
      packages = with nixpkgs.legacyPackages.x86_64-linux; [
        uv
      ];
    };
  };
}
